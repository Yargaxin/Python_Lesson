size = float(input('Enter coat size: '))
height = float(input('Enter your height (meter): '))

class Clothing():
	def __init__(self, size, height):
		self.size = size
		self.height = height
		self.coat_tissue = round(self.size / 6.5 + 0.5, 2)
		self.suit_tissue = round(2 * self.height + 0.3, 2)
		self.all_profit = round(self.coat_tissue + self.suit_tissue, 2)

	def all_prof(self):
		return f'Total tissue consumption: {self.all_profit} meters'

class Coat(Clothing):
	@property
	def coat_formula(self):
		return f'How much fabric does a coat need: {self.coat_tissue}'

class Suit(Clothing):
	def suit_formula(self):
		return f'How much fabric does a suit need: {self.suit_tissue}\n'

clothing = Clothing(size, height)
coat = Coat(size, height)
suit = Suit(size, height)
print(coat.coat_formula)
print(suit.suit_formula())
print(clothing.all_prof())