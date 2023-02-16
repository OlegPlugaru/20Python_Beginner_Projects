def main():
    print("Welcome to the email slicer ")
    print("")

    # collect email from user
    email_input = input("Input your email adress or 'e' for exit: ")
    if email_input == "e" or email_input == "E":
        exit()

    # split the email using the @, the first part as the user name, the second part is gonna be saved as domain
    (username, domain) = email_input.split("@")
    # split domain using ".",
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True:
    main()
