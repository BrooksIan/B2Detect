#!/bin/bash

curl -X ‘GET’ \
  ‘http://127.0.0.1:8000/detectB2obj/777?q=https://farm66.staticflickr.com/65535/52582180138_fddffcbe97_n.jpg’ \
  -H ‘accept: application/json’