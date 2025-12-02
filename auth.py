from fastapi import APIRouter
from passlib.context import CryptContext

router = APIRouter(prefix='/user',tags=['User'])

@router.get('/signup')
async def signup_get(username:str,password:str):
