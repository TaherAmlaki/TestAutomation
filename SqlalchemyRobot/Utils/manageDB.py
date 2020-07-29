from Utils.Base import Base
from Utils.manageSession import manage_session
from Models.TestCaseModel import TestCase
from Models.PeopleModel import People


@manage_session(add_engine=True, add_session=False)
def create_all_tables(engine=None):
    Base.metadata.create_all(bind=engine)
    
