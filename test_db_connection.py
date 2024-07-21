#!/usr/bin/python3

from models import storage

try:
    storage.reload()
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")