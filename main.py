from fastapi import FastAPI, HTTPException, Depends, status, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_depenency = Annotated[Session, Depends(get_db)]



@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_depenency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_depenency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user

