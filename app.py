from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()

postdb = []

#post model
class Post(BaseModel):
    id: int
    title: str
    content: Text
    created_ay: datetime = datetime.now()
    published: Optional[bool] = False

@app.get("/")
def read_root():
    return {"home": "Home Page"}

@app.get("/blog")
def get_posts():
    return postdb

@app.post("/blog")
def add_post(post:Post):
    postdb.append(post.dict())
    return postdb[-1]

@app.get("/blog/{post_id}")
def get_post(post_id:int):
    post = post_id - 1
    return postdb[post]

@app.post("/blog/{post_id}")
def update_post(post_id:int, post:Post):
    postdb[post_id] = post
    return {"message": "Post has been updated successfully"}

@app.delete("/blog/{post_id}")
def delete_post(post_id:int):
    postdb.pop(post_id - 1)
    return {"message": "Post has been deleted successfully"}