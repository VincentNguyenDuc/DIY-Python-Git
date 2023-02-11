import os
from . import commands

def write_tree(directory='.'):
    """
    The file system is a tree => we recursively access all the files 
    in the working directory following depth-first search

    Args:
        directory (str, optional): the current working directory. Defaults to '.'.
    """
    entries = []
    with os.scandir(directory) as it:
        for entry in it:
            full = f'{directory}/{entry.name}'

            # Ignore '.ugit'
            if is_ignored(full):
                continue
            
            # Put all files into object database
            if entry.is_file(follow_symlinks=False):
                type_ = 'blob'
                with open(full, 'rb') as f:
                    object_id = commands.hash_object(f.read())
            
            elif entry.is_dir(follow_symlinks=False):
                type_ = 'tree'
                object_id = write_tree(full)
            
            entries.append((entry.name, object_id, type_))

    # create the tree object
    tree = ' '.join(f'{type_} {object_id} {name}\n' for type_, object_id, name in sorted(entries))
    return commands.hash_object(tree.encode(), 'tree')


def is_ignored(path):
    # ignore .ugit folder
    return '.ugit' in path.split('/')