from fastapi import FastAPI, Header
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

# Headers

@app.get('/get_headers', status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers = {}

    request_headers['ACCEPT'] = accept
    request_headers['CONTENT_TYPE'] = content_type
    request_headers['USER_AGENT'] = user_agent
    request_headers['HOST'] = host

    return request_headers

    