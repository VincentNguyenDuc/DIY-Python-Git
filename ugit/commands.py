import hashlib
import os

GIT_DIR = '.ugit'

def init():
    """
        Initialize a new repo by using os.makedirs
    """
    os.makedirs(GIT_DIR)

def hash_object(data):
    """Hash the content of the file and return the object_id

    Args:
        data (_type_): content of the file
    """
    object_id = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{object_id}', 'wb') as out:
        out.write(data)
    return object_id