from typing import List, Dict, Any 
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from Models.BaseModels.BaseModel import DataModel


class TestCase(DataModel):
    __tablename__ = "testcases"

    test_id = Column(Integer, primary_key=True)
    suite_name = Column(String(50), nullable=False)
    test_name = Column(String(100), nullable=False)
    status = Column(String(20))
    execution_time = Column(DateTime, default=datetime.utcnow)
    
    people = relationship("People", backref=backref("testcase"), lazy="dynamic", cascade="all,delete")

    @classmethod
    def find_by_test_id(cls, test_id: int, session) -> "TestCase":
        return session.query(cls).filter(cls.test_id == test_id).first()

    