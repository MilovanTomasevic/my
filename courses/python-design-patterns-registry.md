---
layout: page
title: Python-Design-Patterns registry
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## registry Model

![](/courses/python-fesign-patterns/behavioral/viz/registry.py.png)

## Python-Design-Patterns registry

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RegistryHolder(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            Here the name of the class is used as key but it could be any class
            parameter.
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)

class BaseRegisteredClass(object):
    __metaclass__ = RegistryHolder
    """
        Any class that will inherits from BaseRegisteredClass will be included
        inside the dict RegistryHolder.REGISTRY, the key being the name of the
        class and the associated value, the class itself.
    """
    pass

if __name__ == "__main__":
    print("Before subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

    class ClassRegistree(BaseRegisteredClass):
        def __init__(self, *args, **kwargs):
            pass

    print("After subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

###  OUTPUT ###
# Before subclassing:
# BaseRegisteredClass
# After subclassing:
# BaseRegisteredClass
# ClassRegistree
```
registry.py
{:.figure}
