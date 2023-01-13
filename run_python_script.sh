#!/bin/bash -x

#Active Python Environment
conda install -n modelCall pip3
conda activate modelCall

#Import Python Libraries  using pip
pip3 install requests
pip3 install pillow
pip3 install numpy
pip3 install image
pip3 install Pillow-PIL

python3 -m PIL callTFB2Model.py $1

#Close Python Environment
conda deactivate modelCall