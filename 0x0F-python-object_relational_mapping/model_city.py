#!/usr/bin/python3
"""
Module containing the City class definition
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    Class representing a city.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        """
        Return a string representation of the City instance.
        """
        return "{}: ({}) {}".format(self.state.name, self.id, self.name)
