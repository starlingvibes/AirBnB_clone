#!/usr/bin/python3
""" """
import datetime
from uuid import UUID
from models.base_model import BaseModel
import unittest


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super.__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
