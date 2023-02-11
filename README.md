# DIY Git using Python

## Table of contents

- [DIY Git using Python](#diy-git-using-python)
  - [Table of contents](#table-of-contents)
  - [General information](#general-information)
  - [Technologies](#technologies)
  - [Project Objectives](#project-objectives)
  - [Set up](#set-up)
  - [Commands](#commands)

## General information

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

## Set up

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
```
