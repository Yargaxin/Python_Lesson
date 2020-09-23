def file():
	try:
		with open('my_file_1.txt', 'w+', encoding='utf-8') as my_file:
			my_text = input('Enter text: ')
			my_file.write(my_text)
			my_file.seek(0)
			read_file = my_file.read()
			print(f'\nFile content: {read_file}')
			print(f'Number of words in file: {len(read_file.split())}')
	except:
		print('Error!')

file()