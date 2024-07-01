import openai
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure OpenAI API

# Database setup
DATABASE_URL = "postgresql://user:password@db:5432/openai_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


Base.metadata.create_all(engine)
