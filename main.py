from fastapi import FastAPI

import uvicorn
from routers import routerpost, routeruser

app = FastAPI()

app.include_router(routerpost.router)
app.include_router(routeruser.router)


@app.get("/")
def root():
    return {"message": "Hi Szkudniki"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
