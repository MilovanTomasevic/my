---
layout: page
title: Python-Design-Patterns chaining_method
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## chaining_method Model

![](/courses/python-fesign-patterns/behavioral/viz/chaining_method.py.png)

## Python-Design-Patterns chaining_method

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class Person(object):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=' ')
        return self.action

class Action(object):
    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=' ')
        return self

    def stop(self):
        print('then stop')

if __name__ == '__main__':

    move = Action('move')
    person = Person('Jack', move)
    person.do_action().amount('5m').stop()

### OUTPUT ###
# Jack move 5m then stop
```
chaining_method.py
{:.figure}

