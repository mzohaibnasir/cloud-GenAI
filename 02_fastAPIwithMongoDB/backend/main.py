from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from model import baseTodoClass
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)
import pdb

# pdb.set_trace()


app = FastAPI()

# React might have port:3000 and our FastAPI might have port:8000, we need backend permission to interact with different port
origins = ["https://localhost:3000", "https://localhost:8001", "*"]

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
async def get_todo():
    response = await fetch_all_todos()
    # breakpoint()
    return response


"""
The difference between the two is the way the response model is specified.
# `@app.get("/api/todo{title}", response_model=baseTodoClass)`
In this syntax, the response_model parameter is explicitly specified as part of the @app.get decorator. This tells FastAPI to use the baseTodoClass class as the response model for this endpoint.
# `@app.get("/api/todo{title}") -> baseTodoClass`
In this syntax, the response model is specified using the -> syntax, which is a shorthand way to specify the response model. This is equivalent to the first syntax, but is a more concise way to specify the response model.
Both syntaxes achieve the same result, which is to specify the response model for the endpoint. However, the first syntax is more explicit and clear, while the second syntax is more concise and shorthand.

"""


@app.get("/api/todo{title}", response_model=baseTodoClass)
async def get_todo_by_id(title: str) -> baseTodoClass:
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO with this title: {title}")


@app.put("/api/todo{title}")
async def put_todo(title: str, desc: str) -> baseTodoClass:
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO with this title: {title}")


@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Succesfully deleted"
    raise HTTPException(404, f"there is no TODO with this title: {title}")


@app.post("/api/todo")
async def post_todo(todo: baseTodoClass) -> baseTodoClass:
    response = await create_todo(todo.model_dump())
    if response:
        return response
    raise HTTPException(400, "Something went wrong/bad request")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8001, log_level="info", reload=True)
