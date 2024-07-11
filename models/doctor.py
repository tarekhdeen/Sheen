#!/usr/bin/python3
"""A doctor Class Module"""

from models.base_model import BaseModel

class Doctor(BaseModel):
    """Doctor class inherits from BaseModel"""

    first_name = ""
    last_name = ""
    specialization = ""
    contact_info = ""
    clinic_id = ""