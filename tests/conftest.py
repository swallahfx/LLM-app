import pytest
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from app import create_app, models

load_dotenv()

import os

db_host = os.getenv("PORT_DB")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_server = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")

# Configure OpenAI API


@pytest.fixture(scope="module")
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{db_user}:{db_password}@{db_server}:5432/{db_name}"
    )

    with app.app_context():
        models.Base.metadata.create_all(models.engine)
        yield app
        # models.Base.metadata.drop_all(models.engine)


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def db_session(app):
    Session = sessionmaker(bind=models.engine)
    session = Session()
    yield session
    session.close()
