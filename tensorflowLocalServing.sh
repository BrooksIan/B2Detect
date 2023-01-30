#!/bin/bash

docker pull tensorflow/serving

#Adding the Version number on model target path is VERY important! 
docker run -t --rm -p 8501:8501 \
 -v "/saved_model:/models/saved_model/1" \
-e MODEL_NAME=saved_model \
tensorflow/serving &
