import os

from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/detectB2obj/{postid}")
def read_item(postid: int, q: Union[str, None] = None):

    os.system('wget ' + q + " -O /tmp/b2images/" + str(postid) +".jpg")
    stream = os.popen('python3 ../appB2Detect/callTFB2Model.py /tmp/b2images/' + str(postid) + ".jpg")
    output = stream.read()
	

    return {output}
