from abc import ABC, abstractmethod

class Clothing(ABC):
	def __init__(self, size):
		self.size = size

	@property
	@abstractmethod
	def formula(self):
		pass

	def __add__(self, other):
		return f'Total fabric: {self.formula + other.formula} metrs'

class Coat(Clothing):
	@property
	def formula(self):
		print(f'How much fabric does a coat need: {round(self.size / 6.5 + 0.5, 2)}')
		return round(self.size / 6.5 + 0.5, 2)

class Suit(Clothing):
	@property
	def formula(self):
		print(f'How much fabric does a suit need: {round(2 * self.size + 0.3, 2)}')
		return round(2 * self.size + 0.3, 2)

coat = Coat(10)
suit = Suit(3)
print(coat + suit)
