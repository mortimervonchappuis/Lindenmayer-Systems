from translator import Translator


axiom = 'F+XF+F+XF'
rules = {
'X': 'XF-F+F-XF+F+XF-F+F-X',
}
mapping = {
'+': 'left',
'-': 'right',
'F': 'move',
}

n = 4
size = 8
angle = 90

Sierpinski = Translator(axiom, rules, mapping, size=size, angle=angle)
Sierpinski(n, position=(size*2**(n+1), 0))
