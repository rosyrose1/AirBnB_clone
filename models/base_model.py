#!/usr/bin/python3
"""This is the BaseModel class that defines all
   all common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Parent class from which all other classes inherit"""

    def __init__(self, *args, **kwargs):
        """Constructor of  a BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns the print/str representation of the
        BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/value pairs of __dict__ of the instance
        a key __class__ added with the class name of
        the object
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
