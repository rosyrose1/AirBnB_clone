#!/usr/bin/python3
"""
    Class State that shate common attributes with BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        Class State that inherits from Base
            Attribute:
                name (str) : empty
    """
    name = ""

    def _init_(self, *args, **kwargs):
        """State constructor"""
        super()._init_(*args, **kwargs)
