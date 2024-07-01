from sqlalchemy import Integer, Column, Text
from . import Base

class QA(Base):
    __tablename__ = 'qa'
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)