# import random
import random
from time import sleep
import pygame
pygame.init()
sound = pygame.mixer.Sound('DiceSimulator/happy.mp3')


def slowet(text) -> str:
    for letter in text:
        print(letter, end='', flush=True)
        sleep(0.11)
    return ""
# define a function to orll the dice


sound.play()
print(
    """
               (( _______
     _______     /\O    O\ 
    /O     /\   /  \      \ 
   /   O  /O \ / O  \O____O\ ))
((/_____O/    \\    /O     /
  \O    O\    / \  /   O  /
   \O    O\ O/   \/_____O/
    \O____O\/ ))          ))
  ((                                               by OlegPlugaru
██████╗ ██╗   ██╗██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
██║        ██║   ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                          
""")


def roll_dice():
    dice_drawing = {
        1: (
            "---------",
            "|       |",
            "|   @   |",
            "|       |",
            "---------",
        ),
        2: (
            "---------",
            "| @     |",
            "|       |",
            "|     @ |",
            "---------",
        ),
        3: (
            "---------",
            "| @     |",
            "|   @   |",
            "|     @ |",
            "---------",
        ),
        4: (
            "---------",
            "| @   @ |",
            "|       |",
            "| @   @ |",
            "---------",
        ),
        5: (
            "---------",
            "| @   @ |",
            "|   @   |",
            "| @   @ |",
            "---------",
        ),
        6: (
            "---------",
            "| @   @ |",
            "| @   @ |",
            "| @   @ |",
            "---------",
        ),

    }
    roll = input(slowet("Roll the dice? (Yes/No): "))
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input(slowet("Roll again? (Yes/No): "))


roll_dice()
# create a dictionary that will have the drawings to the dice
# create a dictionary that will have the values of the dice
