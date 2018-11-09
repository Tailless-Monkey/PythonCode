#!/usr/bin/env python
# coding=utf-8
import turtle
spiral = turtle.Turtle()

for i in range(50):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()
