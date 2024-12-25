from pydantic import BaseModel


class URLCreate(BaseModel):
    url: str


class ShortURL(BaseModel):
    short_id: str
    full_url: str

    class Config:
        orm_mode = True


class URLStats(BaseModel):
    short_id: str
    full_url: str
    visits: int

    class Config:
        orm_mode = True