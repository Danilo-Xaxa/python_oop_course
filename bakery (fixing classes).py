class Donut:
    def __init__(self, flavor, toppings, filling, size):    
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling     
        self.size = size

class Customer:	
    def __init__(self, name, age, address, favorite_dessert):
    	self.name = name
	self.age = age
	self.address = address
	self.favorite_dessert = favorite_dessert

class Cake:
    def __init__(self, flavor, price, quality):
        self.flavor = flavor
	self.price = price
	self.quality = quality
    