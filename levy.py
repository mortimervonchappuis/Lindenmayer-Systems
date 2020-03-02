from translator import Translator


axiom = 'F'
rules = {'F': '+F--F+'}
mapping = {
'F': 'move',
'+': 'left',
'-': 'right',
}

size = 2
angle = 45
n = 16

Levy = Translator(axiom, rules, mapping, size, angle)
Levy(n)
