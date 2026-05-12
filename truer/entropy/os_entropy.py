import os

def get_entropy():
    return os.urandom(64)