from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db

from .. import crud, schemas

router = APIRouter()


@router.get("/items/", tags=["items"], response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.User = Depends(crud.get_current_user)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
