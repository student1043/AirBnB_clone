#!/usr/bin/python3
'''Our file storage script'''
import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dict return """
        return FileStorage.__objects

    def new(self, obj):
        """new object"""
        object = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[object] = obj

    def save(self):
        """serialize the objects to JSON"""
        with open(FileStorage.__file_path, "w") as file:
            dictionary = {}
            for a, b in FileStorage.__objects.items():
                dictionary[a] = b.to_dict()
            ink = json.dumps(dictionary)
            file.write(ink)

    def reload(self):
        """File deserializing"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                info = json.load(file)
                for k in info.values():
                    mydic = k["__class__"]
                    mydic = eval(mydic)
                    object = mydic(**k)
                    self.new(object)
        except:
            pass
