class OfficeEquipment():
	def __init__(self, name, color, year, prise, amount):
		self.name = name
		self.color = color
		self.year = year
		self.prise = prise
		self.amount = amount
		self.data_dict = {'Name':self.name,
						'Color':self.color,
						'Year':f'{self.year}',
						'Prise':f'{self.prise} dollars',
						'Amount':f'{self.amount} units\n'}
		self.main_list = []

	def main(self):
		yes_or_no = None
		name_list = []
		color_list = []
		year_list = []
		prise_list = []
		while True:
			try:
				yes_or_no = input('You want to leave? (y/n)').lower()
				if yes_or_no == 'y':
					break
				else:
					name = input('Enter name: ')
					color = input('Enter color: ')
					year = int(input('Enter year: '))
					prise = int(input('Enter prise: '))
					self.main_list.append(name)
					name_list.append(name)
					color_list.append(color)
					year_list.append(year)
					prise_list.append(prise)
					main_dict = {'Name':name_list, 'Color':color_list, 'Year':year_list, 'Prise':f'{prise_list} dollars'}
					
					for key, value in main_dict.items():
						print(f'{key}:{value}')
					print(f'Amount office equipment: {len(self.main_list)}\n')
			except:
				print('Error!')
	@property
	def warehouse(self):
		for key, value in self.data_dict.items():
			print(f'{key}:{value}')

class Printer(OfficeEquipment):
	def __init__(self, name, color, year, prise, amount, speed):
		super().__init__(name, color, year, prise, amount)
		self.speed = speed

	def __str__(self):#доп характеристики
		return f'Speed: {self.speed}'

class Scanner(OfficeEquipment):
	def __init__(self, name, color, year, prise, amount, optical_r):
		super().__init__(name, color, year, prise, amount)
		self.optical_r = optical_r

	def __str__(self):#доп характеристики
		return f'Optical Resolution: {self.optical_r}'

class Xerox(OfficeEquipment):
	def __init__(self, name, color, year, prise, amount, zoom):
		super().__init__(name, color, year, prise, amount)
		self.zoom = zoom

	def __str__(self):#доп характеристики
		return f'Zoom: {self.zoom}'

printer_1 = Printer('Samsung', 'RED', 2020, 300, 1, 15)
printer_2 = Printer('Asus', 'BLACK', 1999, 140, 2, 10)
xerox = Xerox('Lenovo', 'WHITE', 2000, 156, 2, 9)
scanner = Scanner('Nokia', 'RED', 2020, 300, 1, 15)
scanner.warehouse
print(scanner)
xerox.warehouse
print(xerox)
printer_2.warehouse
print(printer_2)
printer_1.main()
