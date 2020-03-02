from translator import Translator

axiom = 'R'
rules = {'R': 'R+L++L-R--RR-L+', 'L':'-R+LL++L+R--R-L'}
mapping = {
'-': 'left',
'+': 'right',
'R': 'move',
'L': 'move',
}

size = 4
angle = 60
n = 5

Gosper = Translator(axiom, rules, mapping, size=size, angle=angle)
Gosper(n)