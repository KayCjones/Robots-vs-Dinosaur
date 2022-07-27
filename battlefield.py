from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot(input("Name your robot: "))
        self.dinosaur = Dinosaur(input("Name your dinosaur: "))

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to the battlefield. Prepare to fight to the death!")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.robot.attack:
                print(f"{self.robot.name} has attacked {self.dinosaur.name}")
            self.dinosaur.attack(self.robot)    
            if self.dinosaur.attack:
                print(f"{self.dinosaur.name} has attacked {self.robot.name}")
            
    def display_winner(self):
        if self.robot.health > 0:
            print(f"{self.robot.name} wins!")
        else:
            print(f"{self.dinosaur.name} wins!")