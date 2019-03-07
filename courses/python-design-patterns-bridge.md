---
layout: page
title: Python-Design-Patterns bridge
description: >
  Python Design Patterns Tutorial for beginners - Learn Python Design Patterns in simple and easy steps starting from basic to advanced concepts with examples ...
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## bridge Model

![](/courses/python-fesign-patterns/structural/viz/bridge.py.png)

## Python-Design-Patterns bridge

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*References:
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python

*TL;DR80
Decouples an abstraction from its implementation.
"""

# ConcreteImplementor 1/2
class DrawingAPI1(object):
    def draw_circle(self, x, y, radius):
        print('API1.circle at {}:{} radius {}'.format(x, y, radius))

# ConcreteImplementor 2/2
class DrawingAPI2(object):
    def draw_circle(self, x, y, radius):
        print('API2.circle at {}:{} radius {}'.format(x, y, radius))

# Refined Abstraction
class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # high-level i.e. Abstraction specific
    def scale(self, pct):
        self._radius *= pct

def main():
    shapes = (CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 7, 11, DrawingAPI2()))

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()

if __name__ == '__main__':
    main()

### OUTPUT ###
# API1.circle at 1:2 radius 7.5
# API2.circle at 5:7 radius 27.5
```
bridge.py
{:.figure}

## bridge Test

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from structural.bridge import DrawingAPI1, DrawingAPI2, CircleShape

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class BridgeTest(unittest.TestCase):
    def test_bridge_shall_draw_with_concrete_api_implementation(cls):
        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        with patch.object(ci1, 'draw_circle') as mock_ci1_draw_circle, patch.object(
            ci2, 'draw_circle'
        ) as mock_ci2_draw_circle:
            sh1 = CircleShape(1, 2, 3, ci1)
            sh1.draw()
            cls.assertEqual(mock_ci1_draw_circle.call_count, 1)
            sh2 = CircleShape(1, 2, 3, ci2)
            sh2.draw()
            cls.assertEqual(mock_ci2_draw_circle.call_count, 1)

    def test_bridge_shall_scale_both_api_circles_with_own_implementation(cls):
        SCALE_FACTOR = 2
        CIRCLE1_RADIUS = 3
        EXPECTED_CIRCLE1_RADIUS = 6
        CIRCLE2_RADIUS = CIRCLE1_RADIUS * CIRCLE1_RADIUS
        EXPECTED_CIRCLE2_RADIUS = CIRCLE2_RADIUS * SCALE_FACTOR

        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        sh1 = CircleShape(1, 2, CIRCLE1_RADIUS, ci1)
        sh2 = CircleShape(1, 2, CIRCLE2_RADIUS, ci2)
        sh1.scale(SCALE_FACTOR)
        sh2.scale(SCALE_FACTOR)
        cls.assertEqual(sh1._radius, EXPECTED_CIRCLE1_RADIUS)
        cls.assertEqual(sh2._radius, EXPECTED_CIRCLE2_RADIUS)
        with patch.object(sh1, 'scale') as mock_sh1_scale_circle, patch.object(sh2, 'scale') as mock_sh2_scale_circle:
            sh1.scale(2)
            sh2.scale(2)
            cls.assertEqual(mock_sh1_scale_circle.call_count, 1)
            cls.assertEqual(mock_sh2_scale_circle.call_count, 1)
```
test_bridge.py
{:.figure}
