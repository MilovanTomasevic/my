---
layout: page
title: Python-Design-Patterns strategy
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## strategy Model

![](/courses/python-fesign-patterns/behavioral/viz/strategy.py.png)

## Python-Design-Patterns strategy

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
This pattern aims to encapsulate each algorithm and allow them to be
interchangeable. Separating algorithms allows the client to scale
with larger and more complex algorithms, since the client and the
strategies are kept independent of each other.

Having the algorithms as an integral part of the client can cause the
client to be larger and harder to maintain. This is more evident when
supporting multiple algorithms. The separation of client and algorithm
allows us to easily replace and vary the algorithm.

*What does this example do?
Below the 'StrategyExample' is an example of the client while the two
functions; 'execute_replacement1' and 'execute_replacement2' are
examples of the implementation or strategy. In the example we can see
that the client can vary it's 'execute' method by changing the
strategy which is responsible for implementation.

http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
 -written-in-python-the-sample-in-wikipedia
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.

*TL;DR80
Enables selecting an algorithm at runtime.
"""

import types

class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)

def execute_replacement1(self):
    print(self.name + ' from execute 1')

def execute_replacement2(self):
    print(self.name + ' from execute 2')

if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()

### OUTPUT ###
# Strategy Example 0
# Strategy Example 1 from execute 1
# Strategy Example 2 from execute 2
```
strategy.py
{:.figure}

## strategy Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import unittest

class StrategyTest(unittest.TestCase):
    def test_print_output(self):
        """
        Verifies the print output when strategy.py is executed.
        The expected_output is equivalent to the output on the command
        line when running 'python strategy.py'.
        """
        output = subprocess.check_output(["python", "behavioral/strategy.py"])
        expected_output = os.linesep.join(
            ['Strategy Example 0', 'Strategy Example 1 from execute 1', 'Strategy Example 2 from execute 2', '']
        )
        # byte representation required due to EOF returned subprocess
        expected_output_as_bytes = expected_output.encode(encoding='UTF-8')
        self.assertEqual(output, expected_output_as_bytes)
```
strategy.py
{:.figure}
