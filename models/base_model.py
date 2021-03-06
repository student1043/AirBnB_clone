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
        if kwargs:
            for k, value in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(
                                                         value,
                                                         "%Y-%m-%dT%H:%M:%S.%f"
                                                        )
                else:
                    self.__dict__[k] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """ Print the given message """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Save: updates the public instace updated_at """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Dictionary save"""
        mydic = {}
        mydic = self.__dict__.copy()
        mydic["created_at"] = self.created_at.isoformat()
        mydic["updated_at"] = self.updated_at.isoformat()
        mydic["__class__"] = self.__class__.__name__
        return (mydic)
