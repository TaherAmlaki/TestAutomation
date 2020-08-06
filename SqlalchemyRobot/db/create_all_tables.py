from db.Base import Base
from sqlalchemy import create_engine
from Models.TestCaseModel import TestCase
from Models.PeopleModel import People


def create_all_tables():
    engine = create_engine("sqlite:///test.db")
    Base.metadata.create_all(bind=engine)
