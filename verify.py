from fastapi.security import OAuth2PasswordBearer
from auth import login_post,SECRET_KEY,ALGORITHM
from fastapi import Depends,HTTPException
from jose import jwt

oauth_scheme=OAuth2PasswordBearer(tokenUrl='user/login')

def verify_token(token=Depends(oauth_scheme)):
    #print(token)
    try:
        decode_token=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decode_token
    except:
        raise HTTPException(status_code=400,detail='Token invalid or expired')
