#!/usr/bin/python3
""" A module defining a review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ A Review class inheriting from the BaseModel class """
    place_id = ''
    user_id = ''
    text = ''
