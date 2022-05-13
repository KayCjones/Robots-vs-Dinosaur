from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon(name, 30)

    def attack(self, dinosaur):                 # the void function makes it so that there will not be anything returned by the function but the word "void" is not visibly seen. just understood
        pass




