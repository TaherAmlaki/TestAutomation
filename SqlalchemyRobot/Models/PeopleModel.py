from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Date
from Models.BaseModels.BaseModel import DataModel


class People(DataModel):
    __tablename__ = "people"

    person_id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("testcases.test_id", ondelete='CASCADE'), nullable=False)
    name = Column(String(20), nullable=False)
