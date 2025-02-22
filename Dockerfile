FROM pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime
LABEL authors="JSK Robotics Laboratory, The University of Tokyo"

ADD . /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt
RUN pip3 install opencv-python-headless # Override opencv-python-headless to opencv-python

ENTRYPOINT ["python3", "face_identification_server.py"]