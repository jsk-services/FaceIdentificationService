import os
from typing import List
import torch
import FaceIdentificationService_pb2 as Messages
import FaceIdentificationService_pb2_grpc as Services
import grpc
from PIL import Image
from concurrent import futures
from ultralytics import YOLO
import torchvision.transforms as transforms
from InceptionResnetV1 import InceptionResnetV1


class FaceIdentificationServer(Services.FaceIdentificationServiceServicer):
    def __init__(self, detector: YOLO, embedder: InceptionResnetV1, transform: transforms.Compose):
        self._detector = detector
        self._embedder = embedder
        self._transform = transform
        pass

    def Identify(self, request: Messages.FaceIdentificationRequest, context):
        from ultralytics.engine.results import Results
        from io import BytesIO
        
        faces: List[Messages.IdentifiedFace] = []

        image = Image.open(BytesIO(request.Image)).convert('RGB')
        results: Results = self._detector.predict(image, device="cuda")[0]
        
        face_images = []

        for box in results.boxes:
            positions = box.xywh.tolist()[0]
            faces.append(Messages.IdentifiedFace(
                Confidence=box.conf.item(),
                CenterX=int(positions[0]),
                CenterY=int(positions[1]),
                BoxWidth=int(positions[2]),
                BoxHeight=int(positions[3]),
                Embedding=[]
            ))
            face_image = image.crop(box.xyxy[0].tolist())
            face_images.append(self._transform(face_image).to("cuda"))

        face_embeddings = self._embedder.forward(torch.stack(face_images)).detach().cpu().numpy()
        for face_index in range(len(faces)):
            faces[face_index].Embedding.extend(face_embeddings[face_index].tolist())
        
        return Messages.FaceIdentificationResponse(
            Faces=faces
        )


if __name__ == "__main__":
    port = os.environ.get("PORT", 50000)

    print("Preparing models...")
    
    face_detector = YOLO("yolov11l-face.pt")
    face_embedder = InceptionResnetV1(pretrained='vggface2', device="cuda").eval()
    face_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((160, 160)),
    ])

    print("Preparing server...")
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Services.add_FaceIdentificationServiceServicer_to_server(
        FaceIdentificationServer(face_detector, face_embedder, face_transform), 
        server)

    print(f"Server address: [::]:{port}")
    
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()
    pass