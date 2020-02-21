#!/usr/bin/python3
"""City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init definition"""
        super().__init__(*args, **kwargs)
