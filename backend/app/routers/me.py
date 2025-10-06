from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..deps import get_current_user
from .. import schemas, models


router = APIRouter(prefix="", tags=["me"])


@router.get("/me", response_model=schemas.UserPublic)
def me(current: models.User = Depends(get_current_user)):
    return current


@router.patch("/me", response_model=schemas.UserPublic)
def update_me(update: schemas.UserUpdate, db: Session = Depends(get_db), current: models.User = Depends(get_current_user)):
    for field, value in update.model_dump(exclude_unset=True).items():
        setattr(current, field, value)
        db.add(current)
        db.commit()
        db.refresh(current)
    return current