from weapon import Weapon

class Robot:
    def __init__(game, name, health, active_weapon):
        game.name = ""
        game.health = health
        game.active_weapon = Weapon(name, 30)

    def attack(game, dinosaur):                 # the void function makes it so that there will not be anything returned by the function 
        pass




