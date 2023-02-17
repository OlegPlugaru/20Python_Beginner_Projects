def main():
    print("This program converts US dollars to MDL's")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    mdls = convert_to_mdls(dollars)

    print("that is", mdls, "mdls.")


def convert_to_mdls(dollars): return dollars * 18.82


main()
