---
layout: page
title: Python-Design-Patterns adapter
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## adapter Model

![](/courses/python-fesign-patterns/structural/viz/adapter.py.png)

## Python-Design-Patterns adapter

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.

*What does this example do?

The example has classes that represent entities (Dog, Cat, Human, Car)
that make different noises. The Adapter class provides a different
interface to the original methods that make such noises. So the
original interfaces (e.g., bark and meow) are available under a
different name: make_noise.

*Where is the pattern used practically?
The Grok framework uses adapters to make objects work with a
particular API without modifying the objects themselves:
http://grok.zope.org/doc/current/grok_overview.html#adapters

*References:
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

*TL;DR80
Allows the interface of an existing class to be used as another interface.
"""

class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"

class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"

class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"

class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)

class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)

    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}
    >>> objects.append(Adapter(dog, make_noise=dog.bark))
    >>> print(objects[0].original_dict())
    {'name': 'Dog'}
    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> car_noise = lambda: car.make_noise(3)
    >>> objects.append(Adapter(car, make_noise=car_noise))

    >>> for obj in objects:
    ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__

def main():

    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__)
    print(objects[0].original_dict())
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))

if __name__ == "__main__":
    main()

### OUTPUT ###
# {'name': 'Dog'}
# {'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x7f631ba3fb00>>, 'obj': <__main__.Dog object at 0x7f631ba3fb00>}    # noqa flake8
# {'name': 'Dog'}
# A Dog goes woof!
# A Cat goes meow!
# A Human goes 'hello'
# A Car goes vroom!!!
```
adapter.py
{:.figure}

## adapter Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from structural.adapter import Dog, Cat, Human, Car, Adapter

class ClassTest(unittest.TestCase):
    def setUp(self):
        self.dog = Dog()
        self.cat = Cat()
        self.human = Human()
        self.car = Car()

    def test_dog_shall_bark(self):
        noise = self.dog.bark()
        expected_noise = "woof!"
        self.assertEqual(noise, expected_noise)

    def test_cat_shall_meow(self):
        noise = self.cat.meow()
        expected_noise = "meow!"
        self.assertEqual(noise, expected_noise)

    def test_human_shall_speak(self):
        noise = self.human.speak()
        expected_noise = "'hello'"
        self.assertEqual(noise, expected_noise)

    def test_car_shall_make_loud_noise(self):
        noise = self.car.make_noise(1)
        expected_noise = "vroom!"
        self.assertEqual(noise, expected_noise)

    def test_car_shall_make_very_loud_noise(self):
        noise = self.car.make_noise(10)
        expected_noise = "vroom!!!!!!!!!!"
        self.assertEqual(noise, expected_noise)

class AdapterTest(unittest.TestCase):
    def test_dog_adapter_shall_make_noise(self):
        dog = Dog()
        dog_adapter = Adapter(dog, make_noise=dog.bark)
        noise = dog_adapter.make_noise()
        expected_noise = "woof!"
        self.assertEqual(noise, expected_noise)

    def test_cat_adapter_shall_make_noise(self):
        cat = Cat()
        cat_adapter = Adapter(cat, make_noise=cat.meow)
        noise = cat_adapter.make_noise()
        expected_noise = "meow!"
        self.assertEqual(noise, expected_noise)

    def test_human_adapter_shall_make_noise(self):
        human = Human()
        human_adapter = Adapter(human, make_noise=human.speak)
        noise = human_adapter.make_noise()
        expected_noise = "'hello'"
        self.assertEqual(noise, expected_noise)

    def test_car_adapter_shall_make_loud_noise(self):
        car = Car()
        car_adapter = Adapter(car, make_noise=car.make_noise)
        noise = car_adapter.make_noise(1)
        expected_noise = "vroom!"
        self.assertEqual(noise, expected_noise)

    def test_car_adapter_shall_make_very_loud_noise(self):
        car = Car()
        car_adapter = Adapter(car, make_noise=car.make_noise)
        noise = car_adapter.make_noise(10)
        expected_noise = "vroom!!!!!!!!!!"

        self.assertEqual(noise, expected_noise)
```
test_adapter.py
{:.figure}
