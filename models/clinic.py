#!/usr/bin/python3
"""A Clinic Class Module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Clinic(BaseModel, Base):
    """Clinic class inherits from BaseModel"""
    __tablename__ = 'clinics'

    name = Column(String(128))
    address = Column(String(128))
    phone_number = Column(String(128))
    email = Column(String(128))