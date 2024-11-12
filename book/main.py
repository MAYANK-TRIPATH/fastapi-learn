from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return{"message": "First fastapi" }

#path parameters
@app.get('/greet/{name}')
async def greet_name(name:str) -> dict:
    return{"message":f"Hey {name}"}


#for query parameters
@app.get('/greet')
async def query_name(age:str) -> dict:
    return{"message" : f"check" "age"}

#for optional
@app.get('/greet')
async def query_name(ame: Optional[str] = 'User', age: int = 0) -> dict:
    return{"message" : f"Hey {name}", "age" : age}



#Request body - POST

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post('/book')
async def create_book(book_data:BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }