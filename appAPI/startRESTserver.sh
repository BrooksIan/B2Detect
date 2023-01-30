#!/bin/bash

cd appAPI/

uvicorn --host 127.0.0.1 --port 4488 main:app --reload