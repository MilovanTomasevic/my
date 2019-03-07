---
layout: page
title: Python-Design-Patterns parameter_injection
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## parameter_injection Model

![](/courses/python-fesign-patterns//dft/parameter_injection.py.png)

## Python-Design-Patterns parameter_injection

```py
#!/usr/bin/python
# -*- coding : utf-8 -*-
import datetime

"""
Port of the Java example of "Parameter Injection" in
"xUnit Test Patterns - Refactoring Test Code" by Gerard Meszaros
(ISBN-10: 0131495054, ISBN-13: 978-0131495050) accessible in outdated version on
http://xunitpatterns.com/Dependency%20Injection.html.

production code which is untestable:

class TimeDisplay(object):

    def __init__(self):
        self.time_provider = datetime.datetime

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider.now()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment
"""

class TimeDisplay(object):
    def __init__(self):
        pass

    def get_current_time_as_html_fragment(self, time_provider):
        current_time = time_provider.now()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment

class ProductionCodeTimeProvider(object):
    """
    Production code version of the time provider (just a wrapper for formatting
    datetime for this example).
    """

    def now(self):
        current_time = datetime.datetime.now()
        current_time_formatted = "{}:{}".format(current_time.hour, current_time.minute)
        return current_time_formatted

class MidnightTimeProvider(object):
    """
    Class implemented as hard-coded stub (in contrast to configurable stub).
    """

    def now(self):
        current_time_is_always_midnight = "24:01"
        return current_time_is_always_midnight
```
parameter_injection.py
{:.figure}

## parameter_injection Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from dft.parameter_injection import TimeDisplay, MidnightTimeProvider, ProductionCodeTimeProvider, datetime

"""
Port of the Java example of "Parameter Injection" in
"xUnit Test Patterns - Refactoring Test Code" by Gerard Meszaros
(ISBN-10: 0131495054, ISBN-13: 978-0131495050) accessible in outdated version on
http://xunitpatterns.com/Dependency%20Injection.html.

Test code which will almost always fail (if not exactly 12:01) when untestable
production code (have a look into constructor_injection.py) is used:

    def test_display_current_time_at_midnight(self):
        class_under_test = TimeDisplay()
        expected_time = "24:01"
        result = class_under_test.get_current_time_as_as_html_fragment()
        self.assertEqual(result, expected_time)
"""

class ParameterInjectionTest(unittest.TestCase):
    def test_display_current_time_at_midnight(self):
        """
        Would almost always fail (despite of right at/after midnight) if
        untestable production code would have been used.
        """
        time_provider_stub = MidnightTimeProvider()
        class_under_test = TimeDisplay()
        expected_time = "<span class=\"tinyBoldText\">24:01</span>"
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(time_provider_stub), expected_time)

    def test_display_current_time_at_current_time(self):
        """
        Just as justification for working example with the time provider used in
        production. (Will always pass.)
        """
        production_code_time_provider = ProductionCodeTimeProvider()
        class_under_test = TimeDisplay()
        current_time = datetime.datetime.now()
        expected_time = "<span class=\"tinyBoldText\">{}:{}</span>".format(current_time.hour, current_time.minute)
        self.assertEqual(
            class_under_test.get_current_time_as_html_fragment(production_code_time_provider), expected_time
        )
```
test_parameter_injection.py
{:.figure}
