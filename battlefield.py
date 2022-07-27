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
            print(self.battle_phase)
            if self.robot.attack:
                print("Mr. Roboto has made the first attack")
            if self.robot.health <= 0 and self.dinosaur.health <= 0:
                print("Game over.")
        # while both fighters have health greater than 0
        self.robot and self.dinosaurs
        
         # display a winner once self.robot or self.dinosaur health reaches 0
    def display_winner(self):
       pass