---
layout: page
title: Python-Design-Patterns prototype
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## prototype Model

![](/courses/python-fesign-patterns/creational/viz/prototype.py.png)

## Python-Design-Patterns prototype

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
This patterns aims to reduce the number of classes required by an
application. Instead of relying on subclasses it creates objects by
copying a prototypical instance at run-time.

This is useful as it make it easier to derive new kinds of objects,
when instances of the class have only a few different combinations of
state, and when instantiation is expensive.

*What does this example do?
When the number of prototypes in an application can vary, it can be
useful to keep a Dispatcher (aka, Registry or Manager). This allows
clients to query the Dispatcher for a prototype before cloning a new
instance.

Below provides an example of such Dispatcher, which contains three
copies of the prototype: 'default', 'objecta' and 'objectb'.

*TL;DR80
Creates new object instances by cloning prototype.
"""

class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj

class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])

if __name__ == '__main__':
    main()

### OUTPUT ###
# [{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
```
prototype.py
{:.figure}

## prototype Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from creational.prototype import Prototype, PrototypeDispatcher

class TestPrototypeFeatures(unittest.TestCase):
    def setUp(self):
        self.prototype = Prototype()

    def test_cloning_propperty_innate_values(self):
        sample_object_1 = self.prototype.clone()
        sample_object_2 = self.prototype.clone()
        self.assertEqual(sample_object_1.value, sample_object_2.value)

    def test_extended_property_values_cloning(self):
        sample_object_1 = self.prototype.clone()
        sample_object_1.some_value = 'test string'
        sample_object_2 = self.prototype.clone()
        self.assertRaises(AttributeError, lambda: sample_object_2.some_value)

    def test_cloning_propperty_assigned_values(self):
        sample_object_1 = self.prototype.clone()
        sample_object_2 = self.prototype.clone(value='re-assigned')
        self.assertNotEqual(sample_object_1.value, sample_object_2.value)

class TestDispatcherFeatures(unittest.TestCase):
    def setUp(self):
        self.dispatcher = PrototypeDispatcher()
        self.prototype = Prototype()
        c = self.prototype.clone()
        a = self.prototype.clone(value='a-value', ext_value='E')
        b = self.prototype.clone(value='b-value', diff=True)
        self.dispatcher.register_object('A', a)
        self.dispatcher.register_object('B', b)
        self.dispatcher.register_object('C', c)

    def test_batch_retrieving(self):
        self.assertEqual(len(self.dispatcher.get_objects()), 3)

    def test_particular_properties_retrieving(self):
        self.assertEqual(self.dispatcher.get_objects()['A'].value, 'a-value')
        self.assertEqual(self.dispatcher.get_objects()['B'].value, 'b-value')
        self.assertEqual(self.dispatcher.get_objects()['C'].value, 'default')

    def test_extended_properties_retrieving(self):
        self.assertEqual(self.dispatcher.get_objects()['A'].ext_value, 'E')
        self.assertTrue(self.dispatcher.get_objects()['B'].diff)
```
test_prototype.py
{:.figure}
