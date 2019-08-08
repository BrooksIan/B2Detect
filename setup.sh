#!/bin/bash

#Import Python Libriaes using pip
pip install requests
pip install pillow
pip install numpy
pip install image
pip install Pillow-PIL


#Download Post Image Processor nar  - Thank You Tim Spann! 
wget https://github.com/tspannhw/nifi-postimage-processor/releases/download/1.0/nifi-postimage-nar-1.0.nar -O /usr/hdf/current/nifi/lib/nifi-postimage-nar-1.0.nar