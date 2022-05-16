from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('dagger', 30)

    def attack(self, dinosaur):                 # the void function makes it so that there will not be anything returned by the function but the word "void" is not visibly seen. just understood
        dinosaur.health -= self.active_weapon.attack_power            # join parameters together with a "." to scope down the classes when coding outso that python can read it accurately


