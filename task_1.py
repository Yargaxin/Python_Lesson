def file():
	my_text = None
	try:
		with open('my_file.txt', 'w', encoding='utf-8') as my_file:
			while True:
				my_text = input('Enter text: ')
				if not my_text:
					break
				else:
					my_file.write(f'{my_text}\n')
	except:
		print('Error!')
file()
