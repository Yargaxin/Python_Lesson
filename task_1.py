def file():
	my_text = None
	try:
		while True:
			with open('my_file.txt', 'w', encoding='utf-8') as my_file:
				my_text = input('Enter text: ')
				my_file.write(my_text)
				yes_or_no = input('Want to overwrite a file (y/n):').lower()
				if yes_or_no == 'n':
					break
				else:
					pass
	except:
		print('Error!')
file()
