from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Twitter Clone")

app.include_router(auth.router)