from datetime import datetime
from model.tag import TagIn, Tag, TagOut
import service.tag as service
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
# def create(tag_in: TagIn) -> TagIn:
def create(tag_in: TagIn):    
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(), secret = "shhhh")
    return service.create(tag)

@app.get("/{tag_str}", response_model=TagOut)
def get_one(tag_str: str):    
    tag: Tag = service.get(tag_str)
    return tag

