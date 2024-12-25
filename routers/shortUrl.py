from fastapi import APIRouter, Depends,  HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import crud
import schemas
from db import get_db

router = APIRouter(tags=["Short Url"])


@router.post("/shorten", response_model=schemas.ShortURL)
def shorten_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db, url_data.url)


@router.get("/{short_id}")
def redirect_to_full_url(short_id: str, db: Session = Depends(get_db)):
    full_url = crud.get_full_url(db, short_id)
    if not full_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(full_url)


@router.get("/stats/{short_id}", response_model=schemas.URLStats)
def get_url_stats(short_id: str, db: Session = Depends(get_db)):
    stats = crud.get_url_stats(db, short_id)
    if not stats:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return stats
