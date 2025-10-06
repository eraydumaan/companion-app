from fastapi import FastAPI
from .database import Base, engine
from .models import User
from .routers import auth, health, me


app = FastAPI(title="Companion API", version="0.1.0")


# DB tablolarını (MVP) otomatik oluştur
Base.metadata.create_all(bind=engine)


app.include_router(health.router)
app.include_router(auth.router)
app.include_router(me.router)