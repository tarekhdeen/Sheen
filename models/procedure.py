#!/usr/bin/python3
"""A Procedure Class Module"""

from models.base_model import BaseModel

class Procedure(BaseModel):
    """Procedure class inherits from BaseModel"""

    name = ""
    description = ""
    cost = 0.0