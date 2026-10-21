from app.database import get_db
from sqlalchemy import text
from sqlalchemy.orm import Session
from app import models
from app.database import Base, engine

from fastapi import Depends, FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health_check(db:Session = Depends(get_db)):
    
    db.execute(text("SELECT 1"))

    return {"status": "ok", "db": "ok"}