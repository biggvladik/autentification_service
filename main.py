from fastapi import HTTPException, status,FastAPI,Depends


app = FastAPI()


@app.post('/login')
def login(username:str,password:str):
    pass


@app.post('/refresh_token')
def get_refresh_token(access_token:str,refresh_token:str):
    pass



