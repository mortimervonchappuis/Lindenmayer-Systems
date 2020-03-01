import turtle
from lindenmayer import Lindenmayer


class Gosper:
	def __init__(self, size=8, angle=60):
		self.size = size
		self.angle = angle
		self.mapping = {
		'-': lambda: turtle.left(self.angle),
		'+': lambda: turtle.right(self.angle),
		'R': lambda: turtle.forward(self.size),
		'L': lambda: turtle.forward(self.size),
		}
		self.l_sys = Lindenmayer(axiom='R', rules={'R': 'R+L++L-R--RR-L+', 'L':'-R+LL++L+R--R-L'})

	def __call__(self, n):
		turtle.speed(0)
		turtle.hideturtle()
		turtle.penup()
		turtle.setposition((-self.size/2 * 1.25**(n), self.size * 2**(n)))
		turtle.pendown()
		for x in self.l_sys(n):
			if x in self.mapping:
				self.mapping[x]()
		turtle.exitonclick()


gosper = Gosper()
gosper(2)