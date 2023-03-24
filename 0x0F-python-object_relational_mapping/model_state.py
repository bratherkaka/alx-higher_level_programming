#!/usr/bin/python3
"""model_state module

This module defines the State class, which represents the states table in the
MySQL database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class

    This class inherits from Base and represents the states table in the MySQL
    database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
