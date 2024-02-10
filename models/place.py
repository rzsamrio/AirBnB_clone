#!/usr/bin/python3
""" Defines Place Object Class """
from base_model import BaseModel


def Place(BaseModel):
    """ Describes a specific area or location """
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

    def __init__(self, *args, **kwargs):
        """ Initialise the superclass if called """
        super.__init__(*args, **kwargs)
