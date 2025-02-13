def int_checker(question):
    """Checks users enter an integer / float that is more than zero
    (or optional exit code)"""

    error = "please enter an integer"

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    # ask users for their name
    name= input("Name: ") # replace with call to 'not blank' function

    # ask for their age and check it's between 2 and 120
    age = int_checker("Age: ")

    # Output error / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} brought a ticket")
