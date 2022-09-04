#!/usr/bin/python3
""" This module instantiates an object of the FileStorage class """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
