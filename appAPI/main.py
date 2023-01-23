import os
import json

from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# /detectB2obj/${postid}?q=${imageURL}

@app.get("/detectB2obj/{postid}")
def read_item(postid: int, q: Union[str, None] = None):

    os.system('wget ' + q + " -O /tmp/b2images/" + str(postid) +".jpg")
    stream = os.popen('python3 ../appB2Detect/callTFB2Model.py /tmp/b2images/' + str(postid) + ".jpg")
    output = stream.read()
    jsonResponse = json.loads(output)
    
    return {str(jsonResponse)}
