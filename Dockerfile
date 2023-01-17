FROM tensorflow/serving:lastest 

USER root
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install setuptools --upgrade
RUN pip3 install tensorboard pandas tensorflow-serving-api-python3 tensorflow-serving-client-grpc tensorboard-plugin-wit obspy keras-tcn requests pillow numpy image Pillow-PIL
RUN pip3 install tensorflow
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"