#!/usr/bin/python3
"""Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class Des"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Init definition"""
        super().__init__(*args, **kwargs)
