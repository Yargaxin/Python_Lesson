class Cell():
	def __init__(self, amount):
		self.amount = amount

	def __str__(self):
		return self.amount

	def __add__(self, other):
		return self.amount + other.amount

	def __sub__(self, other):
		if self.amount < other.amount:
			print('Negative!')
			return 'Error!'
		else:
			return self.amount - other.amount

	def __mul__(self, other):
		return self.amount * other.amount

	def __truediv__(self, other):
		return round(self.amount / other.amount)

	def make_order(self, rows):
		return (rows * '*' + '\n') * round(self.amount / rows)

cell_1 = Cell(30)
cell_2 = Cell(24)
cell_3 = cell_1 + cell_2
print(f'Add: {cell_3}')
print(f'Sub: {cell_1 - cell_2}')
print(f'Mul: {cell_1 * cell_2}')
print(f'Div: {cell_1 / cell_2}')
print(cell_2.make_order(7))
