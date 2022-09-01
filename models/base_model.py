#!/usr/bin/env python
""" This module defines a base class for our AirBnB project """
import uuid
import datetime


class BaseModel:
    """ A base model class """

    def __init__(self):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Prints a string representation of the class """
        return (f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        """ Updates `updated_at` with the current datetime """
        self.updated_at = datetime.datetime.now()

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
