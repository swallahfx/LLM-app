import pytest
# from app import create_app, models
from app import create_app, models
# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        models.Base.metadata.create_all(models.engine)
        yield app
        models.Base.metadata.drop_all(models.engine)

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def db_session(app):
    Session = sessionmaker(bind=models.engine)
    session = Session()
    yield session
    session.close()
