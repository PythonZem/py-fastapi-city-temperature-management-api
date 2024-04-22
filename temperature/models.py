from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from City.models import DBCity
from db.database import Base


class DBTemperature(Base):
    __tablename__ = "temperatures"

    id = Column(Integer, pk=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    date_time = Column(DateTime, default=datetime.now)
    temperature = Column(Float)

    city = relationship(DBCity, back_populates="temperatures")