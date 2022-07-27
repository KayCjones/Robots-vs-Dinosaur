from timeit import repeat
from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = self.choose_weapon()

    def choose_weapon(self):
        while True:
            user_input = input("Select your weapon from the 3 options: Dagger, Flame Thrower or Scythe \n")
            if user_input == "Dagger":
                return Weapon("Dagger", 30)
            elif user_input == "Flame Thrower":
                return Weapon("Flame Thrower", 40)
            elif user_input == "Scythe":
                return Weapon("Scythe", 35)
            else:
                print("No matching weapon. Choose again.")

    # return choose_weapon(self):

    def attack(self, dinosaur):                 # the void function makes it so that there will not be anything returned by the function but the word "void" is not visibly seen. just understood
        dinosaur.health -= self.active_weapon.attack_power            # join parameters together with a "." to scope down the classes when coding out so that python can read it accurately


