import PIL.Image
from PIL import ImageDraw
import numpy
import requests
from pprint import pprint
import time
import json
import sys


imagePath = str(sys.argv[1])
#output_name = str(sys.argv[2])
threshold=0.95 #= str(sys.argv[3])
timeTheashold = 2.5

image = PIL.Image.open(imagePath)  # Change dog.jpg with your image
image_np = numpy.array(image)
draw = ImageDraw.Draw(image)


payload = {"instances": [image_np.tolist()]}
start = time.time()
res = requests.post("http://public-sector-das0.field.hortonworks.com:8501/v1/models/saved_model:predict", json=payload)
#print(f"Took {time.perf_counter()-start:.2f}s")
processTime = time.time()-start


jsonStr= json.dumps(res.json())
jsonDict = json.loads(jsonStr)

predScore = jsonDict['predictions'][0]['detection_scores'][0]
#topDetectionBox = jsonDict['predictions'][0]['detection_boxes'][0]

if((predScore >= threshold) and (timeTheashold >= processTime)):
	response = {"response":"B2Found","confidence": predScore , "duration": processTime }

else:
	response = {"response":"B2NotFound","confidence":predScore,"duration":processTime}

jsonresponse = json.dumps(response)
print(jsonresponse)
