from model import baseTodoClass

import motor.motor_asyncio  # mongodbdriver


# for connrction between `database.py` and `mongoDB`
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")


database = client.DatabaseTodo
collection = database.todo


# fetch one todo


async def fetch_one_todo(title: str) -> baseTodoClass:
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(baseTodoClass(**document))
    return todos


async def create_todo(todo: str) -> baseTodoClass:
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title: str, desc: str) -> baseTodoClass:
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title: str) -> bool:
    await collection.delete_one({"title": title})
    return True
