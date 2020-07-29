from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def manage_session(add_engine: bool = False, add_session: bool = True):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            engine = create_engine("sqlite:///test.db")
            Session = sessionmaker(bind=engine)
            session = Session()
            exception_: Exception = None 

            if add_engine:
                kwargs['engine'] = engine

            if add_session:
                kwargs['session'] = session

            try:
                res = func(*args, **kwargs)
            except Exception as ex:
                exception_ = ex
            finally:
                session.close()
                if exception_ is not None:
                    raise exception_
                return res

        return wrapper
        
    return decorator