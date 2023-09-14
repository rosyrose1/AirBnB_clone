#!/usr/bin/python3
"""
    Class City that shares common atteibutes with BaseModel
"""
from models.base_model import BaseModel
from uuid import UUID


class City(BaseModel):
    """
        Class city that inherits from BaseModel
            Atrribute:
                state_id (str) - empty, will be
                State.id
                name (str) - empty
    """
    state_id = ""
    name = ""

    def _init_(self, *args, **kwargs):
        """City constructor"""
        super()._init_(*args, **kwargs)
