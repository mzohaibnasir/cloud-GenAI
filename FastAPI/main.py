from fastapi import FastAPI, HTTPException

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
    return "An exceptional Company."


###############################3 TWO ENDPOINTS
# to return list of data
@fastapp.get("/bands")
async def bands() -> list[dict]:
    return BANDS


# to return band by id
@fastapp.get("/bands/{band_id}")
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b["id"] == band_id), None)
    """
    
    
    x = (i for i in BANDS if i["id"] == 2)  # round brackets for generator
    # list(x)
    print(next(x))
    print(next(x))
    print(next(x, "xxx"))
    
    
    """

    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


################################


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
