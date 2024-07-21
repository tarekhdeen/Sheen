#!/usr/bin/python3
"""A Patient Class Module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Patient(BaseModel, Base):
    """Patient class inherits from BaseModel"""
    __tablename__ = 'patients'
    
    name = Column(String(128), nullable=False)
    age = Column(String(128))
    gender = Column(String(128))
    contact_info = Column(String(128))
    medical_history = Column(String(128))