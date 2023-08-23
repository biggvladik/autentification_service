from datetime import datetime
from typing import Optional
from .auth import *
from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr

class User(Document):
    username: str
    password: str
  #  access_token: AccessToken
   # refresh_token:RefreshToken

    @classmethod
    async def by_username(cls,username:str):
        return await cls.find_one(cls.username == username)



class UserAuth(BaseModel):
    username:str
    password:str


