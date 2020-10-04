try:
	length = float(input('Enter length (meters): '))
	width = float(input('Enter width (meters): '))
except:
	print("Numbers!")

class Road():
	def __init__(self, length, width):
		self._length = length
		self._width = width
		self._kilo = 25
		self._centimeters = 5

	def mas(self):
		print(f'Asphalt mass: {round(self._length * self._width * self._kilo * self._centimeters) / 1000} tons')
try:
	r = Road(length, width)
	r.mas()
except:
	print('Error!')