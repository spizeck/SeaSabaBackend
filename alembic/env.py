from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy import create_engine
from alembic import context
import os
from dotenv import load_dotenv

# Import all models here so that they will be registered properly when
from app.db.base_class import Base
from app.users.models import User, UserPreferences, UserProfile
from app.contracts.models import (Hotel, MealOption, RoomType, OccupancyRate, DivingPackage, SpecialOffer,
                                  BookingPolicy, GroupContract, Season)

# Load .env file
load_dotenv()

# Get DATABASE_URL from environment variable
sqlalchemy_url = os.getenv("DATABASE_URL")

# Alembic Config object
config = context.config

# Set the sqlalchemy.url in the Alembic configuration
config.set_main_option("sqlalchemy.url", sqlalchemy_url)

# Logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support
from app.db.base_class import Base

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
