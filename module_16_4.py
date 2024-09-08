from fastapi import FastAPI, status, HTTPException, Body, Path
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str = Path(..., min_length=5, max_length=20, description='Enter username', example='UrbanUser')
    age: int = Path(..., ge=18, le=120, description='Enter age', example=24)


@app.get('/users')
def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
def create_user(username: str = Path(...), age: int = Path(...)):
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user)
    return f'Пользователь {username} добавлен'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str = Path(...), age: int = Path(...)):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f'Пользователь {username} обновлен'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')


@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f'Пользователь {user.username} удален'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')
