#!/usr/bin/python3
""" creates an instance of file storage """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
