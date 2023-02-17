import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Your score is ", str(user_points),
              "Computer score is", str(computer_points))
        if user_points == computer_points:
            print("It's a tie!")
        elif user_points > computer_points:
            print("You Win!!!")
        else:
            print("You Lose!")

        print("Game ended")
        break

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")

        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Paper covers rock, You Lose!")
            computer_points += 1

        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("Rock smashes scissors, You Win!!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is a tie!")

        elif computer_input == "scissor":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Scissors tie paper. You Lose!")
            computer_points += 1

        elif computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("Paper covers rock. You Win!")
            user_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is a tie")

        elif computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Rock smashes scissors, You Lose!")
            computer_points += 1

        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("Scissors cuts paper, You Win!!")
            user_points += 1

    if user_input != "exit" or user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid input, you can choose only ('rock'/'paper'/'scissors')")
