# An Implementation of Git using Python

Source: [Nikita](https://www.leshenko.net/p/ugit/)

## Table of Contents

- [An Implementation of Git using Python](#an-implementation-of-git-using-python)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies](#technologies)
  - [Project Objectives](#project-objectives)
  - [Set Up](#set-up)
  - [Commands](#commands)

## General Information

- In this project, I will try to implement a Git-like version control system called "μgit" from scratch but using Python

- Ugit is not exactly Git, but it shares the important ideas of Git. ugit is way shorter and doesn't implement irrelevant features.

## Technologies

- Python
- Pip
- Git
- Graphviz

## Project Objectives

- Built Git from scratch
- Worked with python packaging system
- Set up a virtual environment for development
- Used SHA-1 for implement "the object database"
- Deepened my understanding into Git
- Tried implemented this in a different language, and object-oriented programming

## Set Up

- Install Pip following this [instruction](https://pip.pypa.io/en/stable/installation/)
- Set up virtual environment following this [instruction](https://docs.python.org/3/library/venv.html)
- Install Graphviz following this [instruction](https://graphviz.org/download/)
- Clone [this repository](https://github.com/VincentNguyenDuc/py-git.git) to your working directory
- Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

- To install 'ugit' into your virtual environment run:

```bash
pip install .
```

## Commands

```bash

# object id: the hash code of the commit / branch
# refs: reference to branch name / tags / object id

# initialize a ugit repository
ugit init

# print contents from object id
ugit cat-file {object_id}

# commit
ugit commit -m 'message'

# tag
ugit tag {name} {object_id}(optional - use for specific commit / if not available then tag the closet commit)

# List all commits from the chosen commit to the beginning of version history. If not specific object id or refs, then list all commits to the current HEAD
ugit log {object_id / refs}(optional)

# check out a branch or a specific commit
ugit checkout {object_id / refs}

# create a branch from a commit, default to the current HEAD
ugit branch {name} {start_point}(optional) 

# show all branches
ugit branch

# visualize the commits history using graphviz
ugit k

# show the information of the current branch
ugit status

# show the differences within a commit
ugit diff {object_id}(optional - default to HEAD)

# show the differences between a commit and its parent
ugit show

# reset to a version of branch, and delete every commits after that version
ugit reset {object_id}
```
