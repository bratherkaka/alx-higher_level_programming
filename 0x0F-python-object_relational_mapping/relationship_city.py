from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

