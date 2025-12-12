from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm,HTTPBearer
from passlib.context import CryptContext
from maindb import Users
from dependency import depend_users,depend_verify
from passlib.hash import sha256_crypt
from datetime import datetime,timedelta
from jose import jwt

router = APIRouter(prefix='/user',tags=['User'])
pwd_context = CryptContext(schemes=['sha256_crypt'],deprecated='auto')
SECRET_KEY='mysecretkey'
ALGORITHM='HS256'
exp_time=15

@router.post('/signup')
async def signup_post(username:str,password:str,sign_service=Depends(depend_users),verify_service=Depends(depend_verify)):
    if verify_service.check_username(username):
        return f'{username} already exist'

    pwd_hash=pwd_context.hash(password)
    sign_service.signup(username,pwd_hash)
    return f'{username} successfully added'

@router.post('/login')
async def login_post(form:OAuth2PasswordRequestForm=Depends(),login_service=Depends(depend_users)):
    username =form.username
    password = form.password
    credentials=login_service.login(username)

    if len(credentials) == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid login')

    id,u_name,pwd=credentials[0]
    check_pwd = pwd_context.verify(password, pwd)
    if not check_pwd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Password invalid')

    exp = datetime.utcnow() + timedelta(minutes=exp_time)
    for_payload = {'id':id,'user':u_name,'exp':int(exp.timestamp())}
    token=jwt.encode(for_payload,SECRET_KEY,algorithm=ALGORITHM)
    return {'access_token':token,'token_type':'bearer','user':{'id':id,'username':u_name}}

#
# #NORMAL LOGIN BACKUP
# @router.post('/login')
# async def login_post(username:str,password:str,login_service=Depends(depend_users),select_all=Depends(depend_verify)):
#     credentials=login_service.login(username)
#
#     if len(credentials) == 0:
#         return 'Invalid username'
#
#     id,u_name,pwd=credentials[0]
#     check_pwd = pwd_context.verify(password, pwd)
#     if not check_pwd:
#         return 'Invalid password'
#
#     exp = datetime.utcnow() + timedelta(minutes=exp_time)
#     for_payload = {'id':id,'user':u_name,'exp':int(exp.timestamp())}
#     token=jwt.encode(for_payload,SECRET_KEY,algorithm=ALGORITHM)
#     return {'access_token':token,'token_type':'bearer','user':{'id':id,'username':u_name}}
#
#





