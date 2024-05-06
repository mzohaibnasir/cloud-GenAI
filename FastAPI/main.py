from fastapi import FastAPI

import uvicorn

fastapp = FastAPI()

# creating list endpoint
BANDS = [
    {"id": 1, "name": "A", "genre": "X"},
    {"id": 2, "name": "B", "genre": "Y"},
    {"id": 3, "name": "C", "genre": "Z"},
]


@fastapp.get("/")
async def index() -> dict[str, int]:
    return {"hello": 786}


@fastapp.get("/about")
async def about() -> str:
    return "An exceptional Company"


if __name__ == "__main__":
    uvicorn.run(
        "main:fastapp", host="127.0.0.1", port=5000, log_level="info", reload=True
    )


############################################################################
"""
The command uvicorn main:app refers to:
    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    
It is equivalent to:
    `from main import app`
"""

""" or uvicorn main:app --reload"""
