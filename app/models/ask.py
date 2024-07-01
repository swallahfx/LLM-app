from sqlalchemy import Column, Integer, Text

from . import Base


class QA(Base):
    __tablename__ = "qa"
    qa_id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
