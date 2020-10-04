import re

data_dict = []
number_list = []

def create_dict():
	try:
		with open('my_text_6.txt', 'r', encoding='utf-8') as my_file:
			for line in my_file:
				line_split = line.split()
				number = re.findall(r'(\d+)', line)# Ищу числа
				map_list = list(map(int, number))
				number_list.append(sum(map_list))
				data_dict.append(line_split[0])
			for key, value in zip(data_dict, number_list):
				print(f'{key}{value}')
	except:
		print('Error!')

create_dict()