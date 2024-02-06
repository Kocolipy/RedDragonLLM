from fastapi import FastAPI
from pydantic import BaseModel

from backend.model import LMMModel

app = FastAPI()
model = LMMModel()

class Query(BaseModel):
    content: str


@app.get("/")
async def root():
    return model.query("Hello. I am a first time user.")

@app.post("/query/")
async def create_query(query: Query):
    print(f'Request received: {query.content}. Generating response...')
    return model.query(query.content)