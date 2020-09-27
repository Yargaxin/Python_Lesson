from random import choice

name = input('Enter the name of your car: ')
color = input('Enter the color of your car: ')
speed = float(input('Enter the speed of your car: '))

info_dict = {'Name':name,
			'Color':color,
			'Speed':speed}

left_or_right = ['Left', 'Right']

class MainCar():
	def __init__(self, name, color, speed, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police
		self.l_or_r = choice(left_or_right)

	def show_info(self):
		print('Your main car\n')
		for key, value in info_dict.items():
			print(f'{key}: {value}')

	def go(self):
		return f'{self.name} Go!'

	def stop(self):
		return f'{self.name} stopped for refueling'

	def turn(self):
		return f'{self.name} turn {self.l_or_r}!'

	def show_speed(self):
		return f'Current vehicle speed: {self.speed} kilometers / hour'

class TownCar(MainCar):
	def __init__(self, name, color, speed, is_police):
		super().__init__(name, color, speed, is_police)

	def show_info(self):
		print('\nYour Town Car:')
		print(f'Name:{self.name}, Color:{self.color}, Speed:{self.speed}\n')

	def show_speed(self):
		super().show_speed()
		if self.speed > 60:
			return f'{self.color} {self.name} speeding! {self.speed} kilometers/hour.Slow down!'
		else:
			return f'No violations! {self.speed} kilometers/hour'

class SportCar(MainCar):
	def __init__(self, name, color, speed, is_police):
		super().__init__(name, color, speed, is_police)
	
	def show_info(self):
		print('\nYour Sport Car')
		print(f'Name:{self.name}, Color:{self.color}, Speed:{self.speed}')

class WorkCar(MainCar):
	def __init__(self, name, color, speed, is_police=None):
		super().__init__(name, color, speed, is_police)
	
	def show_info(self):
		print('\nYour Work Car:')
		print(f'Name:{self.name}, Color:{self.color}, Speed:{self.speed}\n')

	def show_speed(self):
		super().show_speed()
		if self.speed > 40:
			return f'{self.color} {self.name} speeding! {self.speed} kilometers/hour.Slow down!'
		else:
			return f'No violations! {self.speed} kilometers/hour'

class PoliceCar(MainCar):
	def __init__(self, name, color, speed, is_police):
		super().__init__(name, color, speed, is_police)
	def police_car(self):
		print('\nPolice Car!')
		print('It is not yours car but be careful! Do not go fast!')
		print(f'Machine characteristics: {self.speed} kilometers/hour')

mc = MainCar(name, color, speed, False)
tc = TownCar('Mazda', 'Green', 60, False)
wc = WorkCar('Mersedes', 'Red', 120)
pc = PoliceCar('Ford', 'White', 80, True)
sc = SportCar('Tesla', 'Black', 350, False)

#print(sc.go())
#print(tc.turn())
"""mc.show_info()
print(wc.go())
print(mc.show_speed())
print(pc.turn())
print(mc.stop())
tc.show_info()
print(tc.show_speed())
sc.show_info()
print(wc.go())
print(wc.show_speed())
pc.police_car()"""
