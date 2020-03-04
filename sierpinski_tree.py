from translator import Translator
from pathos.multiprocessing import Pool
from threading import Thread


axiom='A'
rules={
'A': '--[FA]+[FA]++[FA]+[FA]',
'F': 'FF'
}
mapping = {
'-': 'left',
'+': 'right',
'F': 'move',
'[': 'remember',
']': 'restore',
}

angle = 45
size = 4
n = 6

#Sierpinski = Translator(axiom, rules, mapping, angle=angle, size=size)
#Sierpinski(n, angle=90, position=(0, 0))
#quit()
for i in range(13, 49, 4):
	from translator import Translator
	p = Pool(4)
	f = lambda x: Translator(axiom, rules, mapping, angle=i+x, size=size)(n, angle=90, name='hollunder')
	p.map(f, range(4))
