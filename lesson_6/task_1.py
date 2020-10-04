import time
from colorama import Fore, Back, Style

class TrafficLight():
	def __init__(self):
		self.__color = ['Red', 'Yellow', 'Green']
		self.color_red = Back.RED
		self.color_yellow = Back.YELLOW
		self.color_green = Back.LIGHTGREEN_EX

	def running(self):
		while True:
			print(Fore.BLACK, end='')
			print(self.color_red, end='')
			print(f'Stop:{self.__color[0]}')
			time.sleep(5)
			print(self.color_yellow, end='')
			print(f'Get ready:{self.__color[1]}')
			time.sleep(2)
			print(self.color_green, end='')
			print(f'Go,Go:{self.__color[2]}')
			time.sleep(4)

traffic = TrafficLight()
traffic.running()
