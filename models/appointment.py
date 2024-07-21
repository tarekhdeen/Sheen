#!/usr/bin/python3
"""An Appointment Class Module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Appointment(BaseModel, Base):
    """Appointment class inherits from BaseModel"""
    __tablename__ = 'appointments'
    
    date = Column(String(128))
    time = Column(String(128))
    procedure = Column(String(128))
    status = Column(String(128))