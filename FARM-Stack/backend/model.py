from pydantic import BaseModel


class baseTodoClass(BaseModel):
    title: str
    description: str
