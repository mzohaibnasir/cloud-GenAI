from fastapi import FastAPI

import uvicorn

fastapp = FastAPI()


@fastapp.get("/")
async def index():
    return {"hello": "world"}


"""

The command uvicorn main:app refers to:

    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    
It is equivalent to:
    `from main import app`
"""


# if __name__ == "__main__":
#     uvicorn.run("main:fastApp", host="127.0.0.1", port=5000, log_level="info")

""" or uvicorn main:app --reload"""
