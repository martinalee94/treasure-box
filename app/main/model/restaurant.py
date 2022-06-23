from setuptools import sic
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.sql.schema import FetchedValue
from app.database.mysql import Base

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(64), nullable = False)
    avg_rating = Column(Float(2))
    address = Column(String(256), nullable = False)
    si_addr = Column(String(16))
    gu_addr = Column(String(32))
    dong_addr = Column(String(64))
    create_date = Column(DateTime, server_default = FetchedValue())
    update_date = Column(DateTime, server_default = FetchedValue())
    is_deleted = Column(SmallInteger, default = 0)

class RestaurantReview(Base):
    __tablename__ = "restaurant_review"

    id = Column(Integer, primary_key = True, autoincrement = True)
    content = Column(String(128))
    rating = Column(Integer)
    create_date = Column(DateTime, server_default = FetchedValue())

