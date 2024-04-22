from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base
from temperature.models import DBTemperature


class DBCity(Base):
    __tablename__ = "cities"

    id = Column(Integer, pk=True, index=True)
    name = Column(String(60), unique=True, nullable=False)
    additional_info = Column(String(550))

    temperature = relationship(DBTemperature, back_populates="city")
