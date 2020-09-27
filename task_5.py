def sum_number():
	try:
		with open('my_text_5.txt', 'w+', encoding='utf-8') as sum_file:
			number = input('Enter numbers: ')
			print(number, file=sum_file)
			split_number = number.split()
			print(sum(map(int, split_number)))
	except:
		print('Error!')

sum_number()