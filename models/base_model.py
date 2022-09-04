#!/usr/bin/python3
""" This module defines a base class for our AirBnB project """
import datetime
import uuid


class BaseModel:
    """ A base model class """

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.datetime.strptime(
                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.datetime.strptime(
                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """ Returns a string representation of the class """
        return (f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        """ Updates `updated_at` with the current datetime """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key-value pairs of __dict__ of the instance """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary.update(
            {"created_at": datetime.datetime.isoformat(self.created_at)})
        dictionary.update(
            {"updated_at": datetime.datetime.isoformat(self.updated_at)})
        return dictionary
