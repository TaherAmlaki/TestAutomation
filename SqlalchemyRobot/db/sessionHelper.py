from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def close_session(session):
    if session is not None:
        session.close()


def create_new_session(session=None):
    close_session(session)

    engine = create_engine("sqlite:///test.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine

