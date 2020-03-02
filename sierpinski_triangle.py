from translator import Translator


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
size = 2
n = 8

Sierpinski = Translator(axiom, rules, mapping, angle=angle, size=size)
Sierpinski(n, (-size * 2**(n-1), size * (-2)**(n-1)), angle=angle)
