from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> dict:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = username, age
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str,
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> dict:
    users[user_id] = username, age
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    users.pop(user_id)
    return f'The user {user_id} is deleted'
