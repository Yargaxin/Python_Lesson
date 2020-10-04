import re
data = input('Enter day and month and year: ')
month_dict = {1:'January',
			2:'February',
			3:'March',
			4:'April',
			5:'May',
			6:'June',
			7:'July',
			8:'August',
			9:'September',
			10:'October',
			11:'November',
			12:'December'}

class Data():
	def __init__(self, data):
		self.data = data
	
	@classmethod
	def find_number(cls, amount):
		cls.amount = amount
		cls.number = re.findall(r'(\d+)', cls.amount)
		cls.num_list = list(map(int, cls.number))

	@staticmethod
	def method_2(month):
		day, month, year = month
		if month > 10 or month == 0 or day > 31 or day == 0:
			print('Wrong!')
		else:
			print(f'{day}st {month_dict[month]} {year} year')

emp_1 = Data(data)
emp_1.find_number(emp_1.data)
try:
	emp_1.method_2(emp_1.num_list)
except:
	print('Little data!')