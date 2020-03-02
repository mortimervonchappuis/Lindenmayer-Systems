from translator import Translator


axiom = 'F'
rules = {
'F': 'F+F-F-FF-F-F-fF',
'f': 'fff'
}
mapping = {
'+': 'left',
'-': 'right',
'F': 'move',
'f': 'move',
}

n = 8

Sierpinski = Translator(axiom, rules, mapping)
Sierpinski(n)
