from weapon import Weapon
from dinosaur import Dinosaur 

weapon_one = Weapon("Dagger", 25)
print(weapon_one.attack_power, weapon_one.name)

dinosaur = Dinosaur(100, 40)
print(dinosaur.health, dinosaur.attack_power)