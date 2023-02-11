import hashlib
import os


GIT_DIR = '.ugit'

def init():
    """
        Initialize a new repo by using os.makedirs
    """
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')

def set_HEAD(oid):
    with open(f'{GIT_DIR}/HEAD', 'w') as f:
        f.write(oid)


def get_HEAD():
    if os.path.isfile(f'{GIT_DIR}/HEAD'):
        with open(f'{GIT_DIR}/HEAD') as f:
            return f.read().strip()

def hash_object(data, type_ = 'blob'):
    """Hash the content of the file and return the object_id

    Args:
        data: content of the file
        type_: type of object, default 'blob'
    """
    obj = type_.encode() + b'\x00' + data
    object_id = hashlib.sha1(obj).hexdigest()
    with open(f'{GIT_DIR}/objects/{object_id}', 'wb') as out:
        out.write(obj)
    return object_id

def get_object(object_id, expected='blob'):
    """
    Get the content of the file from object id
    """
    with open(f'{GIT_DIR}/objects/{object_id}', 'rb') as f:
        obj = f.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content
