from models.user import *
from models.auth import *
from password import hash_password
from fastapi import APIRouter, HTTPException, Depends



router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login(user_auth:UserAuth):
    user = await User.by_username(user_auth.username)
    print(hash_password(user_auth.password))
    if user is None or hash_password(user_auth.password) != user.password:
        raise HTTPException(status_code=401, detail="Bad username or password")
    access_token = 'acess_token'
    refresh_token = 'refresh_token'
    return 'Success'


@router.post("/refresh")
async def refresh():
    pass


