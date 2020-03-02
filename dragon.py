from translator import Translator


axiom = 'FX'
rules = {
'X': 'X+YF+',
'Y': '-FX-Y'
}
mapping = {
'+': 'left',
'-': 'right',
'F': 'move',
}

n = 12
size = 2
position = size/2*((1+1j)**n)

Dragon = Translator(axiom, rules, mapping, size=size)
Dragon(n, position=(int(position.imag), -int(position.real)))