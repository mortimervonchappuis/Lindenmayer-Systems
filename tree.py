import turtle
from lindenmayer import Lindenmayer


class Tree:
	def __init__(self, size=2, angle=45):
		self.stack = []
		self.size = size
		self.angle = angle
		self.stack = []
		self.mapping = {
		'[': lambda: (self.stack.append((turtle.pos(), turtle.heading())), turtle.left(self.angle)),
		']': lambda: (turtle.penup(), turtle.setposition(self.stack[-1][0]), turtle.setheading(self.stack[-1][1]), self.stack.pop(), turtle.pendown(), turtle.right(self.angle)),
		'0': lambda: turtle.forward(self.size),
		'1': lambda: turtle.forward(self.size),
		}
		self.l_sys = Lindenmayer(axiom='0', rules={'1': '11', '0':'1[0]0'})

	def __call__(self, n):
		turtle.speed(0)
		turtle.hideturtle()
		turtle.penup()
		turtle.setheading(90)
		turtle.setposition((0, -self.size * 2**(n-1)))
		turtle.pendown()
		for x in self.l_sys(n):
			if x in self.mapping:
				self.mapping[x]()
		turtle.exitonclick()


tree = Tree()
tree(8)