import time
from typing import Dict
from decouple import config
import jwt
JWT_SECRET = 'very_secret'
JWT_ALGORITHM = 'HS256'


def token_response(token: str):
    return {
        "access_token": token
    }



def signJWT(username: str) -> Dict[str,str]:
    payload = {
        'username': username,
        'expires': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return  token_response(token)



def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None

    except:
        return {}

