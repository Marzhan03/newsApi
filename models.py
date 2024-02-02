from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(DateTime)
    content = Column(String)
    category_id = Column(Integer)
    location_id = Column(Integer)
    site_id = Column(Integer)
    is_read = Column(Boolean, default=False)

# Если у вас есть еще какие-то поля в таблице, добавьте их в модель, чтобы они соответствовали вашей базе данных.
