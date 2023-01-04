from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
#pip install fastapi[all]
#uvicorn main:app to start the server 

class Post(BaseModel):#Post object with strict and unscrict fields 
    title: str
    content: str
    published: bool = True #if this value is not provided, default to true so make this optional
    rating: Optional[int] = None #if not provided, give a value of 'None'


@app.get("/") #decorator turns root() to a path operation 
def root_path():    
    return {"message": "Welcome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):#uses Pydantic to validate the data sent from the front-end
    print(new_post)
    print(new_post.dict())
    return {"data": "new post"}
