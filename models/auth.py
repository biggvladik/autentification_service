from datetime import datetime
from typing import Optional

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr


from datetime import timedelta
from pydantic import BaseModel

class AccessToken(BaseModel):

    value: str
    expires: timedelta = timedelta(minutes=15)



class RefreshToken(BaseModel):

    value: str
    expires: timedelta = timedelta(days=30)


