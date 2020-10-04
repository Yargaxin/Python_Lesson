import numpy as np
from random import randint
rand_m1_left = [randint(121, 590) for i in range(2)]
rand_m1_middle = [randint(45, 100) for i in range(2)]
rand_m1_right = [randint(100, 200) for i in range(2)]
rand_m2_left = [randint(-56, 5) for i in range(2)]
rand_m2_middle = [randint(-360, 700) for i in range(2)]
rand_m2_right = [randint(253, 870) for i in range(2)]

class Matrix():
	def __init__(self, matrix):
		self.matrix = matrix

	def __add__(self, other):
		new_matrix = [[0,0],
						[0,0],
						[0,0]]

		for i in range(len(self.matrix)):
			for j in range(len(other.matrix[i])):
				new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
		return str('\n'.join(['\t '.join([str(j) for j in i]) for i in new_matrix]))
	
	def __str__(self):
		return f'{self.matrix}\n'

m_1 = Matrix([rand_m1_left,rand_m1_middle,rand_m1_right])
m_2 = Matrix([rand_m2_left,rand_m2_middle,rand_m2_right])
m_3 = m_1 + m_2

print(f'Matrix 1: {m_1}')
print(f'Matrix 2: {m_2}')
print(m_3)
