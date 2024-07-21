#!/usr/bin/python3
"""A Procedure Class Module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Procedure(BaseModel, Base):
    """Procedure class inherits from BaseModel"""
    __tablename__ = 'procedures'

    name = Column(String(128))
    description = Column(String(128))
    cost = Column(String(128))