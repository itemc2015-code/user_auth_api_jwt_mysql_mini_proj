from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from verify import verify_token, oauth_scheme
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
@router.post('/delete_user')
async def delete_user(user_id:int,token=Depends(oauth_scheme),delete_service=Depends(depend_users)):
    user=verify_token(token)
    #print(user)
    if user['user'] == 'sanji':
        if user['id'] == user_id:
            return {'message':'account cannot be delete'}

        delete_service.delete_user(user_id)
        return {'message': 'deleted successfully'}

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Not authorized')

