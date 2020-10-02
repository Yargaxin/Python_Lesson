s = '\N{Winking Face}'

class Cell():
	def __init__(self, amount):
		self.amount = amount

	def __add__(self, other):
		return Cell(self.amount + other.amount)

	def __sub__(self, other):
		if self.amount < other.amount:
			print('Negative!')
			return 'Error!'
		else:
			return Cell(self.amount - other.amount)

	def __mul__(self, other):
		return Cell(self.amount * other.amount)

	def __truediv__(self, other):
		return Cell(round(self.amount / other.amount))

	#Add
	def __str__(self):
		return f'{self.amount}'
	#Sub
	def __str__(self):
		return f'{self.amount}'

	#Mul
	def __str__(self):
		return f'{self.amount}'

	#Floordiv
	def __str__(self):
		return f'{self.amount}'

	def make_order(self, rows):
		cells = (rows) * (f'{s} ') * round(self.amount / rows)
		return cells

cell_1 = Cell(6)
cell_2 = Cell(6)
cell_3 = cell_1 + cell_2
print(f'Add: {cell_3}')
print(cell_3.make_order(12))
print(f'Sub: {cell_1.__sub__(cell_2)}')
print(f'Mul: {cell_1.__mul__(cell_2)}')
print(f'Div: {cell_1.__truediv__(cell_2)}')