from fastapi import FastAPI

import uvicorn

fastapp = FastAPI()


@fastapp.get("/")
async def index() -> dict[str, int]:
    return {"hello": 786}


@fastapp.get("/about")
async def about() -> str:
    return "An exceptional Company"


"""

The command uvicorn main:app refers to:

    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    
It is equivalent to:
    `from main import app`
"""


if __name__ == "__main__":
    uvicorn.run(
        "main:fastapp", host="127.0.0.1", port=5000, log_level="info", reload=True
    )

""" or uvicorn main:app --reload"""
