import hashlib

def mix(*sources: bytes):
    return hashlib.sha512(b"".join(sources)).digest()