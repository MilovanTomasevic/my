---
layout: page
title: Python-Design-Patterns command
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## command Model

![](/courses/python-fesign-patterns/behavioral/viz/command.py.png)

## Python-Design-Patterns command

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Encapsulates all information needed to perform an action or trigger an event.
"""

from __future__ import print_function
import os
from os.path import lexists

class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print(u"renaming %s to %s" % (src, dest))
        os.rename(src, dest)

def main():
    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # verify that none of the target files exist
    assert not lexists("foo.txt")
    assert not lexists("bar.txt")
    assert not lexists("baz.txt")
    try:
        with open("foo.txt", "w"):  # Creating the file
            pass

        # they can be executed later on
        for cmd in command_stack:
            cmd.execute()

        # and can also be undone at will
        for cmd in reversed(command_stack):
            cmd.undo()
    finally:
        os.unlink("foo.txt")

if __name__ == "__main__":
    main()

### OUTPUT ###
# renaming foo.txt to bar.txt
# renaming bar.txt to baz.txt
# renaming baz.txt to bar.txt
# renaming bar.txt to foo.txt
```
command.py
{:.figure}

## command Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import unittest
from behavioral.command import MoveFileCommand

class CommandTest(unittest.TestCase):
    @classmethod
    def __get_test_directory(self):
        """
        Get the temporary directory for the tests.
        """
        self.test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_command')

    @classmethod
    def setUpClass(self):
        """
        - Create a temporary directory and file
        /test_command
           /foo.txt
        - get the temporary test directory
        - and initializes the command stack.
        """
        os.mkdir('tests/test_command')
        open('tests/test_command/foo.txt', 'w').close()
        self.__get_test_directory()
        self.command_stack = []
        self.command_stack.append(
            MoveFileCommand(os.path.join(self.test_dir, 'foo.txt'), os.path.join(self.test_dir, 'bar.txt'))
        )
        self.command_stack.append(
            MoveFileCommand(os.path.join(self.test_dir, 'bar.txt'), os.path.join(self.test_dir, 'baz.txt'))
        )

    def test_sequential_execution(self):
        self.command_stack[0].execute()
        output_after_first_execution = os.listdir(self.test_dir)
        self.assertEqual(output_after_first_execution[0], 'bar.txt')
        self.command_stack[1].execute()
        output_after_second_execution = os.listdir(self.test_dir)
        self.assertEqual(output_after_second_execution[0], 'baz.txt')

    def test_sequential_undo(self):
        self.command_stack = list(reversed(self.command_stack))
        self.command_stack[0].undo()
        output_after_first_undo = os.listdir(self.test_dir)
        self.assertEqual(output_after_first_undo[0], 'bar.txt')
        self.command_stack[1].undo()
        output_after_second_undo = os.listdir(self.test_dir)
        self.assertEqual(output_after_second_undo[0], 'foo.txt')

    @classmethod
    def tearDownClass(self):
        """
        Remove the temporary directory /test_command and its content.
        """
        shutil.rmtree('tests/test_command')
```
test_command.py
{:.figure}
