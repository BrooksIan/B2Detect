#!/bin/bash

echo "Install Python Libraries"
./setup.sh 


echo "Launch Model Server"
./tensorflowLocalServing.sh

echo "Launch FastAPI"
./appAPI/startRESTserver.sh

echo "Test Model Server"
./testTFmodelserver.sh

echo "Test REST Server"
./testFASTserver.sh