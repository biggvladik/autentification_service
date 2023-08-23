import time
from typing import Dict
from decouple import config
import jwt
JWT_SECRET = 'very_secret'
JWT_ALGORITHM = 'HS256'
import random
import string




def create_access_token(username: str) -> str:
    payload = {
        'username': username,
        'expires': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return  token



def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None

    except:
        return {}


def create_refresh_token(acces_token:str):
    random_str = ''.join(random.choices(string.ascii_lowercase, k=15))
    temp = acces_token[len(acces_token)-10:len(acces_token)]
    return random_str + temp


