from translator import Translator
from math import sqrt


axiom = 'X' #'F+XF+F+XF'
rules = {
'X': 'XF+XF+XF+', # 'XF-F+F-XF+F+XF-F+F-X',
'F': 'FF',
}
mapping = {
'+': 'left',
'-': 'right',
'F': 'move',
}

n = 6
size = 14
angle = 120

x = size*2**(n-2)
y = sqrt(x**2 - (x/2)**2)*2/3

Sierpinski = Translator(axiom, rules, mapping, size=size, angle=angle)
Sierpinski(n, position=(-x, -y), angle=0)
