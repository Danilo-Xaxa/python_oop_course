class Sprite:    
    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter
 
 
class Enemy(Sprite):
    def __init__(self, x, y, img_file, speed):
        super().__init__(x, y, img_file, speed, 5)
        self.message = "I'm here to protect my master"
 
 
class Player(Sprite):
    def __init__(self, x, y, img_file):
        Sprite.__init__(self, x, y, img_file, 56, 6)
 
 
class DifficultEnemy(Enemy):
    def __init__(self, x, y, img_file, life_counter):
        Enemy.__init__(self, x, y, img_file, speed=80, life_counter=life_counter)
 
 
class EasyEnemy(Player):
    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 40, 1)
        