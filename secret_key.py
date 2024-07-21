#!/usr/bin/python3

import secrets
import string

def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

secret_key = generate_secret_key()
print(secret_key)