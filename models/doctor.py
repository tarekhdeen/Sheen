#!/usr/bin/python3
"""A doctor Class Module"""

from models.base_model import BaseModel,Base
from sqlalchemy import Column, Integer, String

class Doctor(BaseModel, Base):
    """Doctor class inherits from BaseModel"""
    __tablename__ = 'doctors'

    first_name = Column(String(128))
    last_name = Column(String(128))
    specialization = Column(String(128))
    contact_info = Column(String(128))
    clinic_id = Column(Integer())