from translator import Translator


axiom = '[X]+[X]+[X]+'
rules = {
'X': 'F[-F+X][+F-X]',
'F': 'FF' 
}
mapping = {
'F': 'move',
'+': 'left',
'-': 'right',
'[': 'remember',
']': 'restore',
}

size = 5
angle = 120
n = 7

Liz = Translator(axiom, rules, mapping, size, angle)
Liz(n, position=(0, -size*1/3*2**(n-1)), angle=-90)
