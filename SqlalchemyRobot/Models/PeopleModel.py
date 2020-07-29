from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Date
from Utils.Base import Base


class People(Base):
    __tablename__ = "people"

    person_id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("testcases.test_id", ondelete='CASCADE'), nullable=False)
    name = Column(String(20), nullable=False)

    def __repr__(self):
        return f"People(person_id={self.person_id}, test_id={self.test_id}, " \
               f"name={self.name})"
               