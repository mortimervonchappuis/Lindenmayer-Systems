import turtle
from lindenmayer import Lindenmayer


class Plant:
	def __init__(self, size=4, angle=25):
		self.stack = []
		self.size = size
		self.angle = angle
		self.mapping = {
		'F': lambda: turtle.forward(self.size),
		'+': lambda: turtle.left(self.angle),
		'-': lambda: turtle.right(self.angle),
		'[': lambda: self.stack.append((turtle.position(), turtle.heading())),
		']': lambda: (
			turtle.penup(), 
			turtle.setposition(self.stack[-1][0]), 
			turtle.setheading(self.stack[-1][1]), 
			self.stack.pop(), 
			turtle.pendown()
			)
		}
		self.l_sys = Lindenmayer(axiom='X', rules={'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'})


	def __call__(self, n):
		turtle.speed(0)
		turtle.hideturtle()
		turtle.setheading(90-self.angle)
		turtle.penup()
		turtle.setposition((-200, -400))
		turtle.pendown()
		for x in self.l_sys(n):
			if x in self.mapping:
				self.mapping[x]()
		turtle.exitonclick()

farn = Plant()
farn(6)
