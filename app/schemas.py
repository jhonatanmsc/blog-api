from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    title: str
    address: dict
    social_networks: list

    class Config:
        orm_mode = True


class PostSchema(BaseModel):
    lang: str
    title: str
    subtitle: Optional[str] = None
    description: str


class UserRetrieveSchema(UserSchema):
    id: int


class UserUpdateSchema(UserSchema):
    pass


class PostRetrieveSchema(PostSchema):
    id: int
    created_at: datetime
    update_at: datetime


class PostUpdateSchema(PostSchema):
    pass


class PostResumeRetrieveSchema(PostSchema):
    id: int
    created_at: datetime
    update_at: datetime
    company_image: Optional[str] = None
    begin_date: date
    end_date: date


class PostResumeUpdateSchema(PostSchema):
    company_image: Optional[str] = None
    begin_date: date
    end_date: date
