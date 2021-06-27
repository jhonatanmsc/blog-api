from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    title: str
    address: dict
    social_networks: list


class PostSchema(BaseModel):
    lang: str
    title: str
    subtitle: Optional[str] = None
    description: str
    created_at: datetime
    update_at: datetime


class UserRetrieveSchema(UserSchema):
    id: int


class UserUpdateSchema(UserSchema):
    pass


class PostRetrieveSchema(PostSchema):
    id: int


class PostUpdateSchema(PostSchema):
    pass


class PostResumeRetrieveSchema(PostSchema):
    id: int
    company_image: Optional[str] = None
    begin_date: date
    end_date: date


class PostResumeUpdateSchema(BaseModel):
    company_image: Optional[str] = None
    begin_date: date
    end_date: date
