from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaceIdentificationRequest(_message.Message):
    __slots__ = ("Image", "ConfidenceThreshold")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    Image: bytes
    ConfidenceThreshold: float
    def __init__(self, Image: _Optional[bytes] = ..., ConfidenceThreshold: _Optional[float] = ...) -> None: ...

class IdentifiedFace(_message.Message):
    __slots__ = ("Confidence", "CenterX", "CenterY", "BoxWidth", "BoxHeight", "Embedding")
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CENTERX_FIELD_NUMBER: _ClassVar[int]
    CENTERY_FIELD_NUMBER: _ClassVar[int]
    BOXWIDTH_FIELD_NUMBER: _ClassVar[int]
    BOXHEIGHT_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    Confidence: float
    CenterX: int
    CenterY: int
    BoxWidth: int
    BoxHeight: int
    Embedding: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, Confidence: _Optional[float] = ..., CenterX: _Optional[int] = ..., CenterY: _Optional[int] = ..., BoxWidth: _Optional[int] = ..., BoxHeight: _Optional[int] = ..., Embedding: _Optional[_Iterable[float]] = ...) -> None: ...

class FaceIdentificationResponse(_message.Message):
    __slots__ = ("Faces",)
    FACES_FIELD_NUMBER: _ClassVar[int]
    Faces: _containers.RepeatedCompositeFieldContainer[IdentifiedFace]
    def __init__(self, Faces: _Optional[_Iterable[_Union[IdentifiedFace, _Mapping]]] = ...) -> None: ...
