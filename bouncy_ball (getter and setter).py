class BouncyBall:
 
	def __init__(self, price, size, brand):
		self._price = price
		self._size = size
		self._brand = brand
 
	def get_price(self):
		return self._price
 
	def set_price(self, price):
                self._price = price
 
	price = property(get_price, set_price)
 
	def get_size(self):
		return self._size
 
	def set_size(self, size):
                self._size = size
 
	size = property(get_size, set_size)
 
	def get_brand(self):
		return self._brand
 
	def set_brand(self, brand):
                self._brand = brand
 
	brand = property(get_brand, set_brand)
