---
layout: page
title: Python-Design-Patterns iterator
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## iterator Model

![](/courses/python-fesign-patterns/behavioral/viz/iterator.py.png)

## Python-Design-Patterns iterator

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator

*TL;DR80
Traverses a container and accesses the container's elements.
"""

from __future__ import print_function

def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number

# Test the generator
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number, end=' ')

print()

print('Counting to five...')
for number in count_to_five():
    print(number, end=' ')

print()

### OUTPUT ###
# Counting to two...
# one two
# Counting to five...
# one two three four five
```
iterator.py
{:.figure}

