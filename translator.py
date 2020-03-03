import turtle
from lindenmayer import Lindenmayer
from PIL import ImageTk


class Translator:
	def __init__(self, axiom, rules, mapping, size=2, angle=90):
		self.stack = []
		self.size = size
		self.angle = angle
		self.mapping = mapping
		self.lindenmayer_system = Lindenmayer(axiom, rules)

	def move(self):
		turtle.forward(self.size)

	def left(self):
		turtle.left(self.angle)

	def right(self):
		turtle.right(self.angle)

	def remember(self):
		self.stack.append((turtle.position(), turtle.heading()))

	def restore(self):
		turtle.penup()
		pos, ang = self.stack.pop()
		turtle.setposition(pos)
		turtle.setheading(ang)
		turtle.pendown()

	def process(self, x):
		command = self.mapping[x] if x in self.mapping else x
		if command == 'move':
			self.move()
		elif command == 'left':
			self.left()
		elif command == 'right':
			self.right()
		elif command == 'remember':
			self.remember()
		elif command == 'restore':
			self.restore()
		elif type(command) in {tuple, list}:
			for v in enumerate(command):
				self.process(v)
				

	def __call__(self, n, position=(0, 0), angle=90, name=''):
		try:
			turtle.speed(0)
		except:
			pass
		turtle.pencolor('white')
		turtle.getcanvas().config(bg='black')
		turtle.hideturtle()
		turtle.penup()
		turtle.setposition(position)
		turtle.setheading(angle)
		turtle.pendown()
		for i, x in enumerate(self.lindenmayer_system(n)):
			self.process(x)
			#if (i % 27) == 0:
			#	turtle.getcanvas().postscript(file=f"images/deconstruct/sierpinski_{str(i).zfill(4)}.eps")
		#turtle.getcanvas().postscript(file=f"images/deconstruct/sierpinski_{str(i).zfill(4)}.eps")
		if name:
			turtle.getcanvas().postscript(file=f"images/eps/{name}_{str(self.angle).zfill(3)}.eps")#, colormode="color")
			turtle.bye()
		else:
			turtle.exitonclick()

