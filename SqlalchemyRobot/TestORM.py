from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, DateTime, Integer


Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def save(self, session):
        session.add(self)
        session.commit()

    def __repr__(self): 
        return f"Person(id={self.id}, name={self.name}, "\
               f"age={self.age}, timestamp={self.timestamp})" 

"""
creating database, for this to create all tables the models should already
be imported or defined 
"""
engine = create_engine("sqlite:///people.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person()
person.name, person.age = "Taher", 128
person.save(session)

print(person)
