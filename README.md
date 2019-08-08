# B2Detect
## Data Science
### Object Detection on steaming images using Tensorflow and Apache NiFi

## Introduction - B2 Stealth Bomber Social Media Photo Detector <a name="introduction"></a>
The goal of this project is to build an end-to-end project to detect images that contain B2 Stealth Bomber from popular social media sites. 

![result2](https://github.com/BrooksIan/B2Detect/blob/master/images/project/result2.jpg)


**Language**: Python

**Requirements**: 
- Python 2.7
- Tensorflow 1.13

**Author**: Ian R Brooks

**Follow**: [LinkedIn - Ian Brooks PhD](https://www.linkedin.com/in/ianrbrooksphd/)

# Table of Contents
1. [Introduction](#introduction)
2. [Links](#links)
    1. [Apache NiFi](#linksnifi)
    2. [Tensorflow](#linksTF)
 	3. [Additional](#linksAdd)

3. [Setup Environment](#Setup)
	1. [Download Python Libraries](#Setup1)
	2. [Download NiFi Processor](#Setup2)
	3. [Download Project](#Setup3)
	4. [Upload NiFi Templates](#Setup4)

4. [NiFi Configuration](#NifiConfig)
5. [Tensorflow Serving](#TFServe)
6. [Results - Images Posted To Slack](#Result)

## Links <a name="links"></a>
**NiFi Links**: <a name="linksNifi"></a>
- [Posting Images with Apache NiFi 1.7 and a Custom Processor](https://community.hortonworks.com/articles/223916/posting-images-with-apache-nifi-17-and-a-custom-pr.html "link1")
- [Post Images To Slack Custom Processor](https://github.com/tspannhw/nifi-postimage-processor "link2")
- [Great Read On Posting Images to Slack from Apache NiFi Using Custom Processor](https://www.datainmotion.dev/2019/03/posting-images-to-slack-from-apache.html "link3")
- [Uploading NiFi Template](https://www.youtube.com/watch?v=nha90lYQZ-0)

**TensorFlow Links**: <a name="linksTF"></a>
- [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving "link9")
- [Tensorflow Serving Using Docker](https://www.tensorflow.org/tfx/serving/docker "link10")

**Additional Links**: <a name="linksAdd"></a>
- [Ian's Tensorflow Object Detection Tutorial](https://github.com/BrooksIan/LogoTL)
- [Social Searcher](https://www.social-searcher.com/)
- [Slack](https://slack.com/)

## Setup Environment - Download Everything! <a name="Setup"></a>

### Download Python Libraries  <a name="Setup1"></a>

Run at terminal prompt

```bash
pip install requests
pip install pillow
pip install numpy
pip install image
pip install Pillow-PIL
```

### Download NiFi Processor <a name="Setup2"></a>

Run at terminal prompt

```bash
#Download Post Image Processor nar  - Thank You Tim Spann! 
wget https://github.com/tspannhw/nifi-postimage-processor/releases/download/1.0/nifi-postimage-nar-1.0.nar \
-O /usr/hdf/current/nifi/lib/nifi-postimage-nar-1.0.nar
```

### Download Project <a name="Setup3"></a>
Download the project using the git url for [here.](https://github.com/BrooksIan/B2Detect.git) 


### Upload NiFi Template <a name="Setup4"></a>

NiFi flow template is called [B2DetectFlow_BaseTemplate.xml](https://raw.githubusercontent.com/BrooksIan/B2Detect/master/B2DetectFlow_BaseTemplate.xml)

![tempupload](https://github.com/BrooksIan/B2Detect/blob/master/images/project/tempupload.png)

Once the template has been loaded, you should see the following NiFi flow

![nififlow](https://github.com/BrooksIan/B2Detect/blob/master/images/project/nififlow.png)

## NiFi Configuration <a name="NifiConfig"></a>


### Set Social Seacher API Token in InvokeHTTP processor 

![social0](https://github.com/BrooksIan/B2Detect/blob/master/images/project/socialset0.png)

![social1](https://github.com/BrooksIan/B2Detect/blob/master/images/project/socialset1.png)

Set Social Searcher token value

```bash
http://api.social-searcher.com/v2/search?q=B2+Stealth+Bomber&type=photo&key=<YOUR TOKEN VALUE HERE>
```

### SSL Context Configuration in InvokeHTTP processor

![nifissl](https://github.com/BrooksIan/B2Detect/blob/master/images/project/nifissl.png)
![nifissl0](https://github.com/BrooksIan/B2Detect/blob/master/images/project/nifisslcontext0.png)
![nifissl1](https://github.com/BrooksIan/B2Detect/blob/master/images/project/nifisslcontext1.png)

### Post Image Processor Configuration

![postimageprocessor](https://github.com/BrooksIan/B2Detect/blob/master/images/project/postimageprocessor.png)

![postimageconfig](https://github.com/BrooksIan/B2Detect/blob/master/images/project/postimageconfig.png)

Update Slack API Token in URL value: 

```bash
https://slack.com/api/files.upload?token= <YOUR KEY HERE> &channels=b2detect&filename=${absolute.path}${filename}&files:write:user&pretty=1
```

### Put Slack Processor Configuration

![putslack](https://github.com/BrooksIan/B2Detect/blob/master/images/project/putslack.png)

Update Webhook URL value

![slackwebhook](https://github.com/BrooksIan/B2Detect/blob/master/images/project/slackwebhook.png)

## Tensorflow Serving Using Docker <a name="TFServe"></a>

Run at terminal prompt.  Note the path need to point to the location of [saved_model directory](https://github.com/BrooksIan/B2Detect/tree/master/saved_model) in this github repo.

```bash
docker pull tensorflow/serving

#Adding the Version number on model target path is VERY important! 
docker run -p 8900:8500 -p 8501:8501  --mount type=bind,source=/saved_model,target=/models/saved_model/1 \
-e MODEL_NAME=saved_model -t tensorflow/serving &

```

## Configure Execute Stream Command Processor <a name="modelcall"></a>

![steamc0](https://github.com/BrooksIan/B2Detect/blob/master/images/project/streamcommand0.png)

![steamc1](https://github.com/BrooksIan/B2Detect/blob/master/images/project/streamcommand1.png)

1. Download (or copy) callTFModel.py python script to the path set in the Exectute Stream Command processor, which is used to call the Tensorflow model.

2. In callTFModel.py, set the URL of the Tensorflow Docker container

```python
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

image = PIL.Image.open(imagePath)  
image_np = numpy.array(image)
draw = ImageDraw.Draw(image)


payload = {"instances": [image_np.tolist()]}
start = time.time()
res = requests.post("<URL OF DOCKER CONTAINER>:8501/v1/models/saved_model:predict", json=payload)
processTime = time.time()-start


jsonStr= json.dumps(res.json())
jsonDict = json.loads(jsonStr)

predScore = jsonDict['predictions'][0]['detection_scores'][0]

if((predScore >= threshold) and (timeTheashold >= processTime)):
	response = {"response":"B2Found","confidence": predScore , "duration": processTime }

else:
	response = {"response":"B2NotFound","confidence":predScore,"duration":processTime}

jsonresponse = json.dumps(response)
print(jsonresponse)
```


## Results - Images Are Posted To Slack Channel<a name="Result"></a>
![FinalResult](https://github.com/BrooksIan/B2Detect/blob/master/images/project/slackUpload.png)


