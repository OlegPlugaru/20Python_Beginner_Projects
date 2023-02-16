import string
import random

characters = list(string.ascii_letters + string.digits)


def generate_password():
    # If yes, ask for the password lenght
    passsword_lenght = int(
        input("How long would you like your password to be?  "))

    random.shuffle(characters)
    password = []

    # Generate password
    for x in range(passsword_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    # Print password
    print(password)


# Ask user if they want to generate a password or not
option = input("Do you want to generate a password? (Yes/No): ").title()

# If initial response is no, exit program
if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended!")
    exit()
else:
    print("Invalid input, please input Yes or No")
