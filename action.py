from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer
from verify import verify_token
from dependency import depend_verify

router=APIRouter(prefix='/user',tags=['User'])


@router.get('/view_users')
async def view_users(token=Depends(verify_token),user_list=Depends(depend_verify)):
    if token:
        get_lists=user_list.user_info_querry()
        return get_lists