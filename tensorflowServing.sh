docker pull tensorflow/serving

#adding the Version number on model target path is stupidly important! 
docker run -p 8900:8500 -p 8501:8501  --mount type=bind,source=/saved_model,target=/models/saved_model/1 \
-e MODEL_NAME=saved_model -t tensorflow/serving &