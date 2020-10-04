letter = ['Cat\n', 'Dog\n', 'Hello World\n']

def create_file():
	with open('my_file_2.txt', 'w+', encoding='utf-8') as my_file:
		my_file.writelines(letter)
	with open('my_file_2.txt', encoding='utf-8') as my_file:
		line = 0
		word = 0
		for i in my_file:
			line += i.count('\n')
			word = len(i) - 1# - \n
			print(f'{word} in line')
		print(f'Lines: {line}')

create_file()