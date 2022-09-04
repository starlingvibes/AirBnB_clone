#!/usr/bin/python3
""" A module defining a User """
from models.base_model import BaseModel


class User(BaseModel):
    """ A User class inheriting from the BaseModel class """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
