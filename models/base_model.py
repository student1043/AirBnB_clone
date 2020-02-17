#!/usr/bin/python3
"""
BaseModel Class File
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializtion def"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print the given message """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
