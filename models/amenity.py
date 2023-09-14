#!/usr/bin/python3
"""
    Class Amenity that shares common attributes with BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Class Amenity that inherits from BaseModel
        Attribute:
            name (str) - empty
    """
    name = ""

    def _init_(self, *args, **kwargs):
        """Amenity constructor"""
        super()._init_(*args, **kwargs)
