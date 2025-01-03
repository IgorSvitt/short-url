from fastapi import FastAPI
from db import engine
import models
from routers.shortUrl import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
