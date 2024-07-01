# alembic/env.py
from logging.config import fileConfig
from app.models import Base
from sqlalchemy import engine_from_config
from alembic import context
import os

# this is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# add your model's MetaData object here for 'autogenerate' support
# from assessment.app import Base  # Adjust the import according to your app structure

Base

target_metadata = Base.metadata

def get_url():
    user = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "password")
    server = os.getenv("DB_SERVER", "db")  # The service name defined in docker-compose.yml
    db = os.getenv("DB_NAME", "openai_db")
    return f"postgresql+psycopg2://{user}:{password}@{server}/{db}"

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        url=get_url()
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
