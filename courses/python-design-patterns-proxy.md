---
layout: page
title: Python-Design-Patterns proxy
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## proxy Model

![](/courses/python-fesign-patterns/structural/viz/proxy.py.png)

## Python-Design-Patterns proxy

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Provides an interface to resource that is expensive to duplicate.
"""

from __future__ import print_function
import time

class SalesManager:
    def talk(self):
        print("Sales Manager ready to talk")

class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")

class NoTalkProxy(Proxy):
    def talk(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you", "whether he/she is busy or not")

if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

### OUTPUT ###
# Proxy checking for Sales Manager availability
# Sales Manager ready to talk
# Proxy checking for Sales Manager availability
# Sales Manager is busy
# Proxy checking for Sales Manager availability
# This Sales Manager will not talk to you whether he/she is busy or not
# Proxy checking for Sales Manager availability
# This Sales Manager will not talk to you whether he/she is busy or not
```
proxy.py
{:.figure}

## proxy Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from time import time
import unittest
from structural.proxy import Proxy, NoTalkProxy

if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO

class ProxyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Class scope setup. """
        cls.p = Proxy()

    def setUp(cls):
        """ Function/test case scope setup. """
        cls.output = StringIO()
        cls.saved_stdout = sys.stdout
        sys.stdout = cls.output

    def tearDown(cls):
        """ Function/test case scope teardown. """
        cls.output.close()
        sys.stdout = cls.saved_stdout

    def test_sales_manager_shall_talk_through_proxy_with_delay(cls):
        cls.p.busy = 'No'
        start_time = time()
        cls.p.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager ready to talk\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)

    def test_sales_manager_shall_respond_through_proxy_with_delay(cls):
        cls.p.busy = 'Yes'
        start_time = time()
        cls.p.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
Sales Manager is busy\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)

class NoTalkProxyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Class scope setup. """
        cls.ntp = NoTalkProxy()

    def setUp(cls):
        """ Function/test case scope setup. """
        cls.output = StringIO()
        cls.saved_stdout = sys.stdout
        sys.stdout = cls.output

    def tearDown(cls):
        """ Function/test case scope teardown. """
        cls.output.close()
        sys.stdout = cls.saved_stdout

    def test_sales_manager_shall_not_talk_through_proxy_with_delay(cls):
        cls.ntp.busy = 'No'
        start_time = time()
        cls.ntp.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
This Sales Manager will not talk to you whether he/she is busy or not\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)

    def test_sales_manager_shall_not_respond_through_proxy_with_delay(cls):
        cls.ntp.busy = 'Yes'
        start_time = time()
        cls.ntp.talk()
        end_time = time()
        execution_time = end_time - start_time
        print_output = cls.output.getvalue()
        expected_print_output = 'Proxy checking for Sales Manager availability\n\
This Sales Manager will not talk to you whether he/she is busy or not\n'
        cls.assertEqual(print_output, expected_print_output)
        expected_execution_time = 1
        cls.assertEqual(int(execution_time * 10), expected_execution_time)
```
test_proxy.py
{:.figure}
