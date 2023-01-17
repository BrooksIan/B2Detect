#!/bin/bash

#yum install conda

#Active Python Environment
#conda create -n modelCall python=3.8
#conda activate modelCall

#Import Python Libriaes using pip
pip3 install requests
pip3 install pillow
pip3 install numpy
pip3 install image
pip3 install Pillow-PIL

pip3 install fastapi
pip3 install "uvicorn[standard]"

#conda list

#conda deactivate

#Download Post Image Processor nar  - Thank You Tim Spann! 
#wget https://github.com/tspannhw/nifi-postimage-processor/releases/download/1.0/nifi-postimage-nar-1.0.nar -O /usr/hdf/current/nifi/lib/nifi-postimage-nar-1.0.nar