class MyError(Exception):
	def __init__(self, text):
		self.text = text

a = input('Enter number: ')
b = input('Enter number: ')

try:
	a = int(a)
	b = int(b)
	if b == 0:
		raise MyError('ZeroDivison!')
except (ZeroDivisionError, MyError) as err:
	print(err)
else:
	print(f'Divison: {a / b}')