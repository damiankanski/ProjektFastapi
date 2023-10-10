import uvicorn
from fastapi import FastAPI
from routers import routerpost, routeruser

app = FastAPI()

app.include_router(routerpost.router)
app.include_router(routeruser.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)