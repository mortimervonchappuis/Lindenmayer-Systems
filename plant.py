from translator import Translator


axiom = 'X'
rules = {
'X': 'F+[[X]-X]-F[-FX]+X', 
'F': 'FF', 
}
mapping = {
'F': 'move',
'+': 'left',
'-': 'right',
'[': 'remember',
']': 'restore',
}

size = 6
angle = 25
n = 6

Plant = Translator(axiom, rules, mapping, size, angle)
Plant(n, position=(-400, -400), angle=90-angle)