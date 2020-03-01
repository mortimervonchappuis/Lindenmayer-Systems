class Lindenmayer:
	def __init__(self, axiom, rules):
		self.axiom = axiom
		self.rules = rules


	def process(self, string):
		return ''.join(self.rules[x] if x in self.rules else x for x in string)


	def __call__(self, n):
		string = self.axiom
		for _ in range(n):
			string = self.process(string)
		return string


