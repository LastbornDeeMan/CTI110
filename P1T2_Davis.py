"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
# Comment block
"""
for c in ['red', 'green', 'blue', 'purple']:
    t.color(c)
    t.forward(75)
    t.right(90)
"""
"""
t.color("darkred")
t.pensize(5)
#t.penup()
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)

t.color("black")
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
"""

# counting with loops
size = 10
sides = 90
t.color("purple")
for count in range(sides) :
  t.forward(size)
  t.right(360/sides)

t.color("red")
t.circle(150)
t.color("blue")
t.circle(100)
t.right(180)
t.color("darkblue")
t.circle(100)
t.left(90)
t.color("darkblue")
t.circle(100)
t.right(180)
t.color("darkblue")
t.circle(100)
