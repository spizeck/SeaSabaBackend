from app.db.session import SessionLocal

db = SessionLocal()

def get_db():
    try:
        yield db
    finally:
        db.close()