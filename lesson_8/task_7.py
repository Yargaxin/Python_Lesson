class ComplexNum():
	def __init__(self, x):
		self.x = x

	def __add__(self, other):
		return f'Ansver: {self.x + other.x}'

	def __mul__(self, other):
		return f'Ansver: {self.x * other.x}'

complex_num_1 = ComplexNum(complex(input('Enter complex number: ')))
complex_num_2 = ComplexNum(complex(input('Enter complex number: ')))

print(complex_num_1.__add__(complex_num_2))
print(complex_num_1.__mul__(complex_num_2))