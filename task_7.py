import json
import re
negative_dict = {}
average_dict = {}
profit_dict = {}
profit_list_and_negative = [profit_dict, average_dict, negative_dict]
firm_list = []

def json_file():
	with open('my_text_7.txt', 'r', encoding='utf-8') as my_file:
		for line in my_file:
			line_split = line.split()
			number = re.findall(r'(\d+)', line)
			del number[0]
			map_list = list(map(int, number))
			#print(map_list)
			average = 0
			if map_list[0] > map_list[1]:
				profit_dict[line_split[0]] = map_list[0]
				firm_list.append(line_split[0])
				for key, values in profit_dict.items():
					average += values
					average_dict['average'] = round(average / len(firm_list), 2)
			else:
				negative = map_list[1] - map_list[0]
				negative_dict[line_split[0]] = negative
	for key, values in negative_dict.items():
		print(f'Firms that went negative: {key}. Their minus == {values} dollars\n')
		print('-' * 80)
	for key, values in profit_dict.items():
		print(f'\nFirms that went plus: {key}. Their plus == {values} dollars')


json_file()

def create_json_file():
	with open('my_text_7_2.json', 'w', encoding='utf-8') as json_f:
		json.dump(profit_list_and_negative, json_f)


create_json_file()