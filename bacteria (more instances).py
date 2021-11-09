class Bacteria:
    def __init__(self, id, type, age, life_counter, power, x, y):
        self.id = id
        self.type = type
        self.age = age
        self.life_counter = life_counter
        self.power = power
        self.x = x
        self.y = y
 
 
# Create 3 instances of Bacteria
b1 = Bacteria(1, "Cocci", 4, 100, 8, 23, 35)
b2 = Bacteria(2, "Bacilli", 1, 80, 3, 64, 79)
b3 = Bacteria(3, "Vibrios", 2, 60, 6, 75, 19)
