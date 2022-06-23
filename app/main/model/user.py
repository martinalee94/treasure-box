from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import *
from sqlalchemy.sql.schema import FetchedValue

from app.database.mysql import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, autoincrement = True)
    nickname = Column(String(16), nullable = False)
    phone = Column(String(16), nullable = False, unique = True)
    create_date = Column(DateTime, server_default = FetchedValue())
    update_date = Column(DateTime, server_default = FetchedValue())


class SocialUser(Base):
    __tablename__ = "social_user"

    id = Column(Integer, primary_key = True, autoincrement = True)
    social_user_id = Column(String(256), nullable = False)
    social_type = Column(Enum('google', 'kakao', 'naver'), nullable = False)
    user_id = Column(ForeignKey('user.id', ondelete = 'CASCADE', onupdate = 'CASCADE'), index = True)

    user = relationship('User', primaryjoin = 'SocialUser.user_id == User.id')