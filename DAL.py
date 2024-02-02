from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import databases
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from sqlalchemy.orm import sessionmaker
import dotenv, os


dotenv.load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

# Создаем сессию для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

news = sqlalchemy.Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, index=True),
    Column("date", DateTime),
    Column("content", String),
    Column("category_id", Integer),
    Column("location_id", Integer),
    Column("site_id", Integer),
    Column("is_read", Boolean, default=False)
)

