import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Body(BaseModel):
    query: str

@app.get('/')
def root():
    return {
        'response': 'Hello, World!'
    }
