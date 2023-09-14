#!/usr/bin/python3
"""
    Class Review that shares common attributes with BaseModel
"""
from models.base_model import BaseModel
from uuid import UUID


class Review(BaseModel):
    """
        Class Review that inherits from BaseModel
            Attribute:
                place_id (str) - empty, will be
                Place.id
                user_id (str) - empty, will be User.id
                text (str) - empty
    """
    place_id = ""
    user_id = ""
    text = ""

    def _init_(self, *args, **kwargs):
        """Review Constructor"""
        super()._init_(*args, **kwargs)
