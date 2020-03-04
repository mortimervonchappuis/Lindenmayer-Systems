from translator import Translator


axiom = 'X'
rules = {
'X': '-YF+XFX+FY-', 
'Y': '+XF-YFY-FX+', 
}
mapping = {
'F': 'move',
'+': 'left',
'-': 'right',
}

size = 3
n = 8

Hilbert = Translator(axiom, rules, mapping, size)
Hilbert(n, position=(-size * 2**(n-1), -size * 2**(n-1)))