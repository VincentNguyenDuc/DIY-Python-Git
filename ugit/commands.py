import hashlib
import os

GIT_DIR = '.ugit'

def init():
    """
        Initialize a new repo by using os.makedirs
    """
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')

def hash_object(data):
    """Hash the content of the file and return the object_id

    Args:
        data (_type_): content of the file
    """
    object_id = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{object_id}', 'wb') as out:
        out.write(data)
    return object_id

def get_object(object_id):
    """
    Get the content of the file from object id
    """
    with open(f'{GIT_DIR}/objects/{object_id}', 'rb') as f:
        return f.read()
