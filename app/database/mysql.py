from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.database.constants import MYSQL_SERVER_CONF as MSC

conn_url = rf"mysql+pymysql://{MSC['user']}:{MSC['password']}@{MSC['host']}:{MSC['port']}/{MSC['db']}"
engine = create_engine(conn_url)
Base = declarative_base()