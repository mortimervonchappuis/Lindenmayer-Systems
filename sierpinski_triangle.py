from translator import Translator
from math import sqrt


axiom='A'
rules={
'A': 'B-A-B', 
'B':'A+B+A', 
}
mapping = {
'-': 'left',
'+': 'right',
'A': 'move',
'B': 'move',
}

angle = 60
size = 3.5
n = 7


x = (size * 2**(n-1))
y = -sqrt(x**2 - (x/2)**2)*2/3

Sierpinski = Translator(axiom, rules, mapping, angle=angle, size=size)
Sierpinski(n, (x, y), angle=180-angle) # (size * 2**(n-1), -size * (-2)**(n-1))
