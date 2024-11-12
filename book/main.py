from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return{"message": "First fastapi" }


@app.get('/greet/{name}')
async def greet_name(name:str) -> dict:
    return{"message":f"Hey {name}"}


#for query parameters
@app.get('/greet/')
async def query_name(age:str) -> dict:
    return{"message" : f"check" "age"}