from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from model import baseTodoClass

app = FastAPI()

# React might have port:3000 and our FastAPI might have port:8000, we need backend permission to interact with different port
origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.get("/api/todo")
async def get_todo() -> list[baseTodoClass]:
    return 1


@app.get("/api/todo{id}")
async def get_todo_by_id(id: int) -> baseTodoClass:
    return id


@app.put("/api/todo{id}")
async def put_todo(id: int, data: str):
    return 1


@app.delete("/api/todo{id}")
async def delete_todo(id: int):
    return id


@app.post("/api/todo{id}")
async def post_todo(id):
    return id


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, log_level="info", reload=True)
