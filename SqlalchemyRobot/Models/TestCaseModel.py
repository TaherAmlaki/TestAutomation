from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from Utils.Base import Base 


class TestCase(Base):
    __tablename__ = "testcases"

    test_id = Column(Integer, primary_key=True)
    suite_name = Column(String(50), nullable=False)
    test_name = Column(String(100), nullable=False)
    status = Column(String(20))
    execution_time = Column(DateTime, default=datetime.utcnow)
    
    people = relationship("People", backref=backref("testcase"), lazy="dynamic", cascade="all,delete")

    def __repr__(self):
        return f"TestCase(test_id={self.test_id}, suite_name={self.suite_name}, "\
               f"test_name={self.test_name}, status={self.status}, " \
               f"execution_time={self.execution_time})"
