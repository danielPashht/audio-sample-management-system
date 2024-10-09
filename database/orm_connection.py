from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.connection import get_db_url
from contextlib import contextmanager

engine = create_engine(get_db_url(), echo=True)
Session = sessionmaker(bind=engine)


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
