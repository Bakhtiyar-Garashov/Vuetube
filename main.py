from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from starlette.requests import Request

app = FastAPI(title="First project", version="0.0.1")


# a response custom type
class Response(BaseModel):
    message: str
    slug: Optional[str]
    query_param: Optional[str]


@app.get('/')
async def home(request: Request):
    return {"message": "Yeaahh,it worked"}


@app.post('/{slug}')
async def index(request: Request, slug: str, q: Optional[str]) -> Response:
    data = Response(message="Salam", slug=slug, query_param=q)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
