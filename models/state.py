#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Definition"""
        super().__init__(*args, **kwargs)
