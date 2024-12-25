import random, string
from sqlalchemy.orm import Session
import models


def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_short_url(db: Session, full_url: str):
    short_id = generate_short_id()
    while db.query(models.ShortURL).filter(models.ShortURL.short_id == short_id).first():
        short_id = generate_short_id()

    short_url = models.ShortURL(short_id=short_id, full_url=full_url)
    db.add(short_url)
    db.commit()
    db.refresh(short_url)
    return short_url


def get_full_url(db: Session, short_id: str):
    url = db.query(models.ShortURL).filter(models.ShortURL.short_id == short_id).first()
    if url:
        url.visits += 1
        db.commit()
        return url.full_url
    return None


def get_url_stats(db: Session, short_id: str):
    return db.query(models.ShortURL).filter(models.ShortURL.short_id == short_id).first()