from fastapi import FastAPI
import uvicorn
from Routers import routerpost, routeruser

from database import engine
from DataBaseModel import user, post
user.Base.metadata.create_all(bind=engine)
post.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routerpost.router)
app.include_router(routeruser.router)


@app.get("/")
def root():
    return {"message": "Hi Szkudniki"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
