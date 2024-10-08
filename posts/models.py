from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from datebase import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

