#!/usr/bin/python3
""" A module to serialize instances to JSON and deserialize JSON to an instance object"""
import json


class FileStorage:
    """ JSON <--> Instance serializer/deserializer """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Class constructor """
        pass

    def all(self):
        """ Returns the objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds new object to storage dictionary """
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """ Serializes objects to a JSON file """
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """ Deserializes the JSON file to __objects only if the file exists, otherwise catch any exceptions """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State
        }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass


# p = FileStorage()
# print(p.new({'id': '6afad3ca-a07c-4b42-acf1-f187cdd02b11', 'created_at': '2022-09-01T16:54:37.530665',
#              'updated_at': '2022-09-01T16:54:37.530665', '__class__': 'BaseModel'}))
