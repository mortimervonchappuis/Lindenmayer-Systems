from translator import Translator


axiom = 'F'
rules = {'F': '+F--F+'}
mapping = {
'F': 'move',
'+': 'left',
'-': 'right',
}

size = 3.6
angle = 45
n = 12

Levy = Translator(axiom, rules, mapping, size, angle)
Levy(n, position=(-size * 2**(n/2-1), -size*n), angle=0, name='levy')
