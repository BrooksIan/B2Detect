# B2Detect
## Data Science
### Object Detection on steaming images using Tensorflow and Apache NiFi

## Introduction - Corporate Logo Object Detection <a name="introduction"></a>
The goal of this project is to build a 

![result1](https://github.com/BrooksIan/B2Detect/blob/master/Images/project/result1.jpg)
![result2](https://github.com/BrooksIan/B2Detect/blob/master/Images/project/result2.jpg)
![result3](https://github.com/BrooksIan/B2Detect/blob/master/Images/project/result3.jpg)


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
    3. [Ian's Tensorflow Object Detection Tutorial](https://github.com/BrooksIan/LogoTL)

3. [Setup Environment](#Setup)
	1. [Download Python Libraries](#Setup1)
	2. [Download NiFi Processor](#Setup2)
	3. [Download Project](#Setup3)
	4. [Upload NiFi Template](#Setup4)

4. [NiFi Configuration](#NifiConfig)
5. [Tensorflow Serving](#TFServe)
6. [Results - Images Posted To Slack](#Result)

## Links <a name="links"></a>
**NiFi Links**: <a name="linksNifi"></a>
- [Posting Images with Apache NiFi 1.7 and a Custom Processor](https://community.hortonworks.com/articles/223916/posting-images-with-apache-nifi-17-and-a-custom-pr.html "link1")
- [Post Images To Slack Custom Processor](https://github.com/tspannhw/nifi-postimage-processor "link2")
- [Great Read On Posting Images to Slack from Apache NiFi Using Custom Processor](https://www.datainmotion.dev/2019/03/posting-images-to-slack-from-apache.html "link3")

**TensorFlow Links**: <a name="linksTF"></a>
- [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving "link9")
- [Tensorflow Serving Using Docker](https://www.tensorflow.org/tfx/serving/docker "link10")


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

## NiFi Configuration <a name="NifiConfig"></a>


## Tensorflow Serving <a name="TFServe"></a>

Run at terminal prompt


```bash
docker pull tensorflow/serving

#Adding the Version number on model target path is VERY important! 
docker run -p 8900:8500 -p 8501:8501  --mount type=bind,source=/saved_model,target=/models/saved_model/1 \
-e MODEL_NAME=saved_model -t tensorflow/serving &

```

## Result - Images Posted To Slack <a name="Result"></a>
