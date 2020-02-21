#!/usr/bin/python3
"""Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Definition"""
        super().__init__(*args, **kwargs)
