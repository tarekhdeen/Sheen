#!/usr/bin/python3
"""A Patient Class Module"""

from models.base_model import BaseModel


class Patient(BaseModel):
    """Patient class inherits from BaseModel"""

    name = ""
    age = ""
    gender = ""
    contact_info = ""
    medical_history = ""