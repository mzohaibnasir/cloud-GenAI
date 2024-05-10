from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandDataClass

# from enum import Enum
import uvicorn

fastapp = FastAPI()


# class GenreURLChoices(Enum):
#     X = "x"
#     Y = "y"
#     Z = "z"


# creating list endpoint
BANDS = [
    {"id": 1, "name": "A", "genre": "X"},
    {"id": 2, "name": "B", "genre": "Y"},
    {"id": 3, "name": "C", "genre": "Z"},
    {"id": 3, "name": "S", "genre": "Z"},
    {
        "id": 4,
        "name": "Abc",
        "genre": "XYZ",
        "albums": [{"title": "Title", "release_date": "1971-07-21"}],
    },
]


@fastapp.get("/")
async def index() -> dict[str, int]:
    return {"hello": 786}


@fastapp.get("/about")
async def about() -> str:
    return "An exceptional Company."


###############################3 TWO ENDPOINTS
# to return list of data
# @fastapp.get("/bands")
# async def bands() -> list[dict]:
#     return BANDS


@fastapp.get("/bands")
async def bands() -> list[BandDataClass]:
    return [BandDataClass(**b) for b in BANDS]  # with BandDataClass we have validation


# to return band by id
"""
@fastapp.get("/bands/{band_id}", status_code=200)
async def band(band_id: int) -> dict:
    band = next(
        (b for b in BANDS if b["id"] == band_id), None
    )  # next( iterator, default) # one value not multiple values at a time

    # x = (i for i in BANDS if i["id"] == 2)  # round brackets for generator
    # # list(x)
    # print(next(x))
    # print(next(x))
    # print(next(x, "xxx"))

    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band
"""


@fastapp.get("/bands/{band_id}", status_code=200)
async def band(band_id: int) -> BandDataClass:
    band = next(
        (BandDataClass(**b) for b in BANDS if b["id"] == band_id), None
    )  # next( iterator, default) # one value not multiple values at a time

    # x = (i for i in BANDS if i["id"] == 2)  # round brackets for generator
    # # list(x)
    # print(next(x))
    # print(next(x))
    # print(next(x, "xxx"))

    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


# @fastapp.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: str) -> list[dict]:
#     return [b for b in BANDS if b["genre"].lower() == genre.lower()]


# @fastapp.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
#     return [b for b in BANDS if b["genre"].lower() == genre.value]


@fastapp.get("/bands/genre/{genre}")
async def bands_for_genre(genre: GenreURLChoices) -> list[BandDataClass]:
    return [BandDataClass(**b) for b in BANDS if b["genre"].lower() == genre.value]


# GenreURLChoices will return more descriptive error

################################


if __name__ == "__main__":  # code to be executed only when the script is run directly
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
