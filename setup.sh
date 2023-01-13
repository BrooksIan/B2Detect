#!/bin/bash

yum install conda

#Active Python Environment
conda create -n modelCall python=3.8
conda activate modelCall

#Import Python Libriaes using pip
conda install requests
conda install pillow
conda install numpy
#conda install image
#conda install Pillow-PIL

conda list

conda deactivate

#Download Post Image Processor nar  - Thank You Tim Spann! 
#wget https://github.com/tspannhw/nifi-postimage-processor/releases/download/1.0/nifi-postimage-nar-1.0.nar -O /usr/hdf/current/nifi/lib/nifi-postimage-nar-1.0.nar