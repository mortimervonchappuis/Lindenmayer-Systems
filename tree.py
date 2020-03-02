from translator import Translator


axiom = '0'
rules = {
'1': '11', 
'0':'1[0]0', 
}
mapping = {
'[': ('remember', 'left'),
']': ('restore', 'right'),
'0': 'move',
'1': 'move',
}

size = 2
angle = 45
n = 8

Tree = Translator(axiom, rules, mapping, size=size, angle=angle)
Tree(n, position=(0, -size*2**(n-1)))