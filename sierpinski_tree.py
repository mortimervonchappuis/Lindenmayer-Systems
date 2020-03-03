from translator import Translator
from pathos.multiprocessing import Pool
from threading import Thread


axiom='A'
rules={
'A': '[FA]+[FA]--[FA]+',
'F': 'FF'
}
mapping = {
'-': 'left',
'+': 'right',
'F': 'move',
'A': 'move',
'[': 'remember',
']': 'restore',
}

angle = 120
size = 4
n = 6

Sierpinski = Translator(axiom, rules, mapping, angle=angle, size=size)
Sierpinski(n, angle=90)

#for i in range(61, 170, 12):
#	from translator import Translator
#	p = Pool(4)
#	f = lambda x: Translator(axiom, rules, mapping, angle=i+x, size=size)(n, angle=90, name='sierpinski_tree')
#	p.map(f, range(0, 12, 3))
