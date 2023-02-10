import argparse
import os
import sys

from . import commands


def main():
    args = parse_args()
    args.func(args)


def parse_args():
    """parse arguments from the commands

    Returns:
        _type_: _description_
    """
    parser = argparse.ArgumentParser ()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    # ugit init
    init_parser = commands.add_parser ('init')
    init_parser.set_defaults (func=init)

    # ugit hash_object {file_name}
    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    # ugit cat-file {object_id}
    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    return parser.parse_args()


def init(args):
    """
    Initialize a ugit repository (creating a .ugit folder)
    """
    commands.init()
    print(f'Initialized empty ugit repository in {os.getcwd()}/{commands.GIT_DIR}')

def hash_object(args):
    with open(args.file, 'rb') as f:
        print(commands.hash_object(f.read()))

def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(commands.get_object(args.object))


