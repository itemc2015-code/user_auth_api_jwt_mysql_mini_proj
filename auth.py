from fastapi import APIRouter,Depends
from passlib.context import CryptContext
from maindb import Users
from dependency import depend

router = APIRouter(prefix='/user',tags=['User'])
pwd_context = CryptContext(schemes='bcrypt',deprecated='auto')

@router.get('/signup')
async def signup_post(username:str,password:str,sign_service=Depends(depend)):
    sign_service.signup(username,password)
    return f'{username} successfully added'
