---
layout: page
title: Python-Design-Patterns factory_method
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## factory_method Model

![](/courses/python-fesign-patterns/creational/viz/factory_method.py.png)

## Python-Design-Patterns factory_method

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""*What is this pattern about?
The Factory Method pattern can be used to create an interface for a
method, leaving the implementation to the class that gets
instantiated.

*What does this example do?
The code shows a way to localize words in two languages: English and
Greek. "getLocalizer" is the factory method that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "get" will be called
in the same way independently of the language.

*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django:
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns For
example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.

*References:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
https://fkromer.github.io/python-pattern-references/design/#factory-method
https://sourcemaking.com/design_patterns/factory_method

*TL;DR80
Creates objects without having to specify the exact class.
"""

class GreekGetter(object):

    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))

class EnglishGetter(object):

    """Simply echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)

def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

if __name__ == '__main__':
    # Create our localizers
    e, g = get_localizer(language="English"), get_localizer(language="Greek")
    # Localize some text
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))

### OUTPUT ###
# dog σκύλος
# parrot parrot
# cat γάτα
# bear bear
```
factory_method.py
{:.figure}

## factory_method Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.factory_method import get_localizer

class TestLocalizer(unittest.TestCase):
    def setUp(self):
        self.e, self.g = get_localizer(language="English"), get_localizer(language="Greek")

    def test_parrot_eng_localization(self):
        self.assertEqual(self.e.get('parrot'), 'parrot')

    def test_parrot_greek_localization(self):
        self.assertEqual(self.g.get('parrot'), 'parrot')

    def test_dog_eng_localization(self):
        self.assertEqual(self.e.get('dog'), 'dog')

    def test_dog_greek_localization(self):
        self.assertEqual(self.g.get('dog'), 'σκύλος')

    def test_cat_eng_localization(self):
        self.assertEqual(self.e.get('cat'), 'cat')

    def test_cat_greek_localization(self):
        self.assertEqual(self.g.get('cat'), 'γάτα')

    def test_bear_eng_localization(self):
        self.assertEqual(self.e.get('bear'), 'bear')

    def test_bear_greek_localization(self):
        self.assertEqual(self.g.get('bear'), 'bear')
```
test_factory_method.py
{:.figure}
