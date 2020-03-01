import turtle
from lindenmayer import Lindenmayer


class Hilbert:
	def __init__(self, size=4):
		self.size = size
		self.mapping = {
		'F': lambda: turtle.forward(self.size),
		'-': lambda: turtle.left(90),
		'+': lambda: turtle.right(90),
		}
		self.l_sys = Lindenmayer(axiom='X', rules={'X': '-YF+XFX+FY-', 'Y':'+XF-YFY-FX+'})

	def __call__(self, n):
		turtle.speed(0)
		turtle.hideturtle()
		turtle.penup()
		turtle.setposition((-self.size * 2**(n-1), -self.size * 2**(n-1)))
		turtle.pendown()
		for x in self.l_sys(n):
			if x in self.mapping:
				self.mapping[x]()
		turtle.exitonclick()


hilbert = Hilbert()
hilbert(7)