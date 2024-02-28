
from sqlalchemy import Float
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date

from .database import Base


class Driver(Base):
    __tablename__ = "driver_driver"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    driving_score = Column(Float)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now())

