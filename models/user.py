#!/usr/bin/python3
"""
    Class User sharing common attributes with BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel

        Attributes:
            email: (str) - empty
            password: (str) - empty
            first_name: (str) - empty
            last_name: (str) - empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def _init_(self, *args, **kwargs):
        """
            User constructor
        """
        super()._init_(*args, **kwargs)
