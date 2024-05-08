"""

Pydantic allows us to create classes that inherit from BaseModels. 
These classes contain fields that define the structure of piece of data

Pydantic's BaseModel class is a powerful tool for defining data structures in Python. Here's a detailed explanation:

## Pydantic BaseModels:

1. BaseModels are classes that inherit from `pydantic.BaseModel`
2. They provide a way to define the schema (structure) of data objects for validation, serialization, and deserialization.
3. Each field in a BaseModel represents a piece of data within the overall structure.
## Defining Fields:

1. You define fields within a BaseModel class using type annotations (similar to static typing in other languages).
2. These annotations specify the expected data type for each field.


# Type annotations are a that provides a way to specify the expected data type for variables, function arguments, and return values
"""

from pydantic import BaseModel


class User(BaseModel):
    name: str  # Name of the user (string)
    age: int  # Age of the user (integer)
    is_active: bool = True  # User status (boolean, default True)
