#!/bin/bash -x

#Active Python Environment
conda activate modelCall

python3 callTFB2Model.py $1

#Close Python Environment
conda deactivate