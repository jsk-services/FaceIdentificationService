import datetime

import grpc

import FaceIdentificationService_pb2 as Messages
import FaceIdentificationService_pb2_grpc as Services


if __name__ == "__main__":
    with open("test_image_300.png", "rb") as file:
        image = file.read()
    
    timestamp = datetime.datetime.now()
    
    with grpc.insecure_channel('localhost:50000') as channel:
        stub = Services.FaceIdentificationServiceStub(channel)
        response = stub.Identify(Messages.FaceIdentificationRequest(Image=image))
        
        print(f"Time taken: {(datetime.datetime.now() - timestamp).microseconds / 1000} ms")
        
        print(f"Response received: {len(response.Faces)} faces detected.")
        pass