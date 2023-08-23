from app import app
from routers.AuthRouter import   router as AuthRouter




app.include_router(AuthRouter)




# @app.post('/login')
# def login(username:str,password:str):
#     # Проверяем соответсвие логина и пароля
#     access_token = create_access_token(username)
#     refresh_token = create_refresh_token(access_token)
#     return {
#         'access_token': access_token,
#         'refresh_token':refresh_token
#     }
#
#
# @app.post('/refresh_token')
# def get_refresh_token(access_token:str,refresh_token:str):
#     pass
#
#
#     # Ищем в БД такой же refresh_token
#
# @app.post('/registration/')
# async def create_user(user:User):
#     await user.create()
#     return user