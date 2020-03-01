import turtle
from lindenmayer import Lindenmayer


class Sierpinski:
	def __init__(self, size=2, angle=60):
		self.size = size
		self.angle = angle
		self.mapping = {
		'+': lambda: turtle.left(self.angle),
		'-': lambda: turtle.right(self.angle),
		'A': lambda: turtle.forward(self.size),
		'B': lambda: turtle.forward(self.size),
		}
		self.l_sys = Lindenmayer(axiom='A', rules={'A': 'B-A-B', 'B':'A+B+A'})

	def __call__(self, n):
		turtle.speed(0)
		turtle.hideturtle()
		turtle.penup()
		turtle.setposition((-self.size * 2**(n-1), self.size * (-2)**(n-1)))
		turtle.pendown()
		for x in self.l_sys(n):
			if x in self.mapping:
				self.mapping[x]()
		turtle.exitonclick()


sierpinski = Sierpinski()
sierpinski(8)