#!/usr/bin/python3
"""
    Class Place that shares common attributes with BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Class place that inherits from BaseModel
        Attribute:
            city_id (str) - empty, will be City.id
            user_id (str) - empty, will be User.id
            name (str) - empty
            description (str) - empty
            number_rooms (int) - 0
            number_bathrooms (int) - 0
            max_guest (int) - 0
            price_by_night (int) - 0
            latitude  (float) - 0.0
            longitude (float) - 0.0
            amenity_ids (list) - empty list of strings
            later it will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def _init_(self, *args, **kwargs):
        """Place constructor"""
        super()._init_(*args, **kwargs)
