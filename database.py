from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:1234@localhost/SIERRA_LEO_CONCERT_DB"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
