from datetime import datetime


from sqlalchemy import Column, Integer, DateTime, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    lang = Column(String)
    title = Column(String(50))
    subtitle = Column(String(50), nullable=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())


class PostResume(Base):
    __tablename__ = "project_posts"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    lang = Column(String)
    title = Column(String(50))
    subtitle = Column(String(50), nullable=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())
    company_image = Column(String, nullable=True)
    begin_date = Column(Date)
    end_date = Column(Date)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    address = Column(JSON)
    social_networks = relationship("Social", back_populates="user")


class Social(Base):
    __tablename__ = "social_networks"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String)
    icon = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="social_networks")
