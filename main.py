from fastapi import FastAPI,Depends
from auth import router
from verify import  verify_token

app = FastAPI()
app.include_router(router)

@app.get('/protected')
async def protected(user=Depends(verify_token)):
    return {'message':'authorized','user':user}

