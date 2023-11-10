from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:SeeD0409!@localhost:5432/SeaSaba"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For async SQL operations
database = Database(DATABASE_URL)
