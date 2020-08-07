from typing import List, Dict, Any
from db.Base import Base 


class DataModel(Base):
    __abstract__ = True

    def save(self, session):
        session.add(self)
        session.commit()
        session.refresh(self)
    
    def delete(self, session):
        session.delete(self)
        session.commit()

    def update(self, session):
        session.commit()

    def to_dict(self) -> Dict[str, Any]:
        col_names = type(self).__table__.columns.keys()
        return {col_name: getattr(self, col_name, None) for col_name in col_names}

    def __repr__(self):
        cls_name = type(self).__name__ 
        data = [f"{col_name}={col_val}" for col_name, col_val in self.to_dict().items()]
        return f"{cls_name}({', '.join(data)})"        

