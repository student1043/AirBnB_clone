#!/usr/bin/python3
'''Our file storage script'''
import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage"""

    def __init__(self):
        """initialization"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """dict return """
        return self.__objects

    def new(self, obj):
        """new object"""
        object = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[object] = obj

    def save(self):
        """serialize the objects to JSON"""
        with open(self.__file_path, "w") as file:
            dictionary = {}
            for a, b in self.__objects.items():
                dictionary[a] = b.to_dict()
            ink = json.dumps(a)
            file.write(ink)

    def reload(self):
        """File deserializing"""
        try:
            file_reload = open(self.__file_path, "r")
            file = json.loads(file_reload.read())
            for k, v in file.items():
                v = eval(v["__class__"])(**v)
                self.__objects[k] = v
        except:
            pass
