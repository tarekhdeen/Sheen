#!/usr/bin/python3
"""Module for creating a unique FileStorage instance"""
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
