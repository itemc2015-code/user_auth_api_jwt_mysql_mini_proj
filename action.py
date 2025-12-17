from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from verify import verify_token
from dependency import depend_verify,depend_users
from passlib.context import CryptContext

router=APIRouter(prefix='/user',tags=['User'])
pwd_context=CryptContext(schemes=['sha256_crypt'],deprecated='auto')

@router.get('/view_users')
async def view_users(token=Depends(verify_token),user_list=Depends(depend_verify)):
    if token:
        get_lists=user_list.user_info_querry()
        return get_lists
@router.post('/change_password')
async def change_password(pwd:str,token=Depends(verify_token),user_service=Depends(depend_users)):
    if token:
        #print(token)
        hashed_password=pwd_context.hash(pwd)
        user_service.change_pwd(hashed_password,token['user'])
        print(pwd_context.verify(pwd,hashed_password))
        return {'message':'password updated'}
