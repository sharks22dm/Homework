from fastapi import FastAPI, HTTPException, Path, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int = Path(ge=1, le=100, description='Enter User ID', example=1)
    username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')
    age: int = Path(ge=18, le=120, description='Enter age', example=24)


@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
async def get_user(request: Request,
                   user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> User:
    user = User(id=1, username=username, age=age)
    if not users:
        user.id = 1
    else:
        user.id = max(user.id for user in users) + 1
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        deleted_user = users.pop(user_id - 1)
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')
