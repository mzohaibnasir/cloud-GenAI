# it includes pydantic classes we are going to use
# we are going to have any sort of data we have in the application as well as model classes that define the structure of data
#
from enum import Enum
from pydantic import BaseModel
from datetime import date


class GenreURLChoices(Enum):
    X = "x"
    Y = "y"
    Z = "z"


# some bands ma y have none, or mu;ltiple albums
class Album(BaseModel):
    title: str
    release_date: date


class BandDataClass(BaseModel):
    # { 'id':1. 'name':'the band', 'genre': 'rock}
    id: int
    name: str
    genre: str
    albums: list[Album] = []  # name: annotation type = default_value
