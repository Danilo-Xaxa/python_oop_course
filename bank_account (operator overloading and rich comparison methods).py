class BankAccount:

	def __init__(self, name, amount):
		self.name = name
                self.amount = amount
		
	def __lt__(self, other):
		return self.amount < other.amount
	
	def __le__(self, other):
		return self.amount <= other.amount
	
	def __eq__(self, other):
		return self.amount == other.amount
	
	def __ne__(self, other):
		return self.amount != other.amount
	
	def __gt__(self, other):
		return self.amount > other.amount
	
	def __ge__(self, other):
		return self.amount >= other.amount
