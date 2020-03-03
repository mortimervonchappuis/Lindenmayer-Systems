from translator import Translator


axiom = 'X'
rules = {
'X': '-YF+XFX+FY-', 
'Y':'+XF-YFY-FX+', 
}
mapping = {
'F': 'move',
'+': 'left',
'-': 'right',
}

size = 4
n = 6

Hilbert = Translator(axiom, rules, mapping, size)
Hilbert(n, position=(-size * 2**(n-1), -size * 2**(n-1)))