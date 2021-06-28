from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.settings import get_db

Base = declarative_base()

session = next(get_db())


class Model:

    @classmethod
    def objects(cls, **kwargs):
        if kwargs != {}:
            if kwargs.get('id'):
                return session.query(cls).filter(cls.id == kwargs['id']).first()
        return session.query(cls).all()

    def save(self):
        session.add(self)
        session.commit()
        session.refresh(self)
        return True

    def delete(self):
        session.delete(self)
        session.commit()
        session.refresh(self)
        return True


class Post(Model, Base):
    __tablename__ = "posts"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    lang = Column(String)
    title = Column(String(50))
    subtitle = Column(String(50), nullable=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())


class PostResume(Model, Base):
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


class User(Model, Base):
    __tablename__ = "users"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    address = Column(JSON, nullable=True)
    social_networks = relationship("Social", back_populates="user")

    def find_social(self, title):
        for social in self.social_networks:
            if social.title == title:
                return social
        return None

    def save_social(self, networks):
        for social in networks:
            m_social = self.find_social(social['title'])
            if m_social:
                m_social.title = social['title']
                m_social.description = social['description']
                m_social.icon = social['icon']
                m_social.user_id = social['user_id']
                m_social.save()
            else:
                s = Social(
                    title=social['title'],
                    description=social['description'],
                    icon=social['icon'],
                    user_id=social['user_id'],
                )
                s.save()


class Social(Model, Base):
    __tablename__ = "social_networks"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String)
    icon = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="social_networks")
