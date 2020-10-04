class MyError(Exception):
	def __init__(self, text):
		self.text = text

data_list = []
data = None
while True:
	try:
		data = int(input('Enter numbers or exit(0): '))
		if data != int(data):
			raise MyError('Numbers!')
		elif data == 0:
			break
		else:
			data_list.append(data)
		
	except (ValueError, MyError) as mye:
		print(mye)

print(data_list)
