name = input('Enter your name: ')
surname = input('Enter your surname: ')
position = input('Enter your position: ')

wage = float(input('Enter your wage: '))
bonus = float(input('Enter your bonus: '))

income_dict = {'Wage':wage, 
			'Bonus':bonus}
int_list = []

class Worker():
	def __init__(self, name, surname, position):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = income_dict 

class Position(Worker):
	def __init__(self, name, surname, position):
		super().__init__(name, surname, position)

	def get_full_name(self):
		return f'Name:{self.name}, Surname:{self.surname}, Position:{self.position}'

	def get_total_income(self):
		for key, value in income_dict.items():
			print(f'{key}:{value}')
			int_list.append(value)
			print(f'Total:{round(sum(int_list))}')

pos = Position(name, surname, position)
print(pos.get_full_name())
print(pos.get_total_income())