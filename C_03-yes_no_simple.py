def yes_no(question):
    """Checks that users enter yes / y or no / n when prompted"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes (y) or no (n).\n")




# Main routine goes here
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"You chose {want_instructions}\n")