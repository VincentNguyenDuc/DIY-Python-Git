import argparse
import os
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

    # ugit hash_object

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


