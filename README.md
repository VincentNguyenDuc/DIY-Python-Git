# An Implementation of Git using Python

## Table of Contents

- [An Implementation of Git using Python](#an-implementation-of-git-using-python)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies](#technologies)
  - [Project Objectives](#project-objectives)
  - [Set Up](#set-up)
  - [Commands](#commands)
  - [Underlying Implementation](#underlying-implementation)

## General Information

- In this project, I will try to implement a Git-like version control system called "μgit" from scratch but using Python

- ugit is not exactly Git, but it shares the important ideas of Git. ugit is way shorter and doesn't implement irrelevant features.

## Technologies

- Python
- pip
- git

## Project Objectives

- Built Git from scratch
- Worked with python packaging system
- Set up a virtual environment for development
- Used SHA-1 for implement "the object database"

## Set Up

- Install pip following [instruction](https://pip.pypa.io/en/stable/installation/)
- Clone [this repository](https://github.com/VincentNguyenDuc/DIY-Python-Git.git)
- Within the DIY-Python-Git directory, select the Python interpreter (where pip installed)
- Run:

```bash
pip install .
```

## Commands

```bash
# initialize a ugit repository
ugit init

# hash object for storage
ugit hash-object {file_name}

# print contents from object id
ugit cat-file {object_id}

# storing the whole directory
ugit write-tree

# restore a previous version
ugit read-tree {object_id}
```

## Underlying Implementation
