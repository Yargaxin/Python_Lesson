class Stationery():
	def __init__(self, title):
		self.title = title
	
	def draw(self):
		return 'Start rendering'

class Pen(Stationery):
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		return self.title

class Pencil(Stationery):
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		return self.title

class Handle(Stationery):
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		return self.title

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
stationery = Stationery('Handle')

print(pen.draw())
print(pencil.draw())
print(handle.draw())
print(stationery.draw())