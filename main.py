from fastapi import FastAPI,Depends,HTTPException,status
from auth import router
from verify import  verify_token
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
app.include_router(router)

@app.get('/protected')
async def protected(user=Depends(verify_token)):
    return {'message':'authorized','user':user}
