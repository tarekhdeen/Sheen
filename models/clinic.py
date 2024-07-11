#!/usr/bin/python3
"""A Clinic Class Module"""

from models.base_model import BaseModel

class Clinic(BaseModel):
    """Clinic class inherits from BaseModel"""

    name = ""
    address = ""
    phone_number = ""
    email = ""