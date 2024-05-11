from model import baseTodoClass

import motor.motor_asyncio  # mongodbdriver


# for connrction between `database.py` and `mongoDB`
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")


database = client.DatabaseTodo
collection = database.todo


# fetch one todo


async def fetch_one_todo(title) -> baseTodoClass:
    document = await.collection.find_one({
        "title":title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(baseTodoClass(**document)
    return todos
    
    
    
async create_todo()