from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

import os

db_host = os.getenv("PORT_DB")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_server = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")

# Configure OpenAI API

# Database setup
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_server}:5432/{db_name}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


Base.metadata.create_all(engine)
