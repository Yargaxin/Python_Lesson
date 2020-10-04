salary_dict = {'Ivanov':10000, 'Petrov':15000, 'Sidorov':25000,
			'Petrovsky':26000, 'Kotov':18000, 'Sobakin':21000}

addition_list = []

def salary():
	try:
		with open('my_text_3.txt', 'w', encoding='utf-8') as my_file:
			for key, value in salary_dict.items():
				print(f'{key}:{value}', file=my_file)
				if value < 20000:
					print(f'{key} salary: {value}')
				addition_list.append(value)
			sum_addition_list = sum(addition_list)
			average = sum_addition_list / len(key)
			print(f'\nAverage:{average:.2f}')

	except:
		print('Error!')

salary()
