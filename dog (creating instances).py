class Dog:
    
    def __init__(self, age, name, is_male, weight):
        self.age = age
        self.name = name
        self.is_male = is_male # Boolean. True if Male, False if Female.
        self.weight = weight
        
# Create your instance below this line
my_dog = Dog(5, "Yogi", True, 15)
