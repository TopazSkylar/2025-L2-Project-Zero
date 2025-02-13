def num_checker(question, num_type, exit_code=None):
    """Checks users enter an integer / float that is more than zero
    (or optional exit code)"""

    if num_type == "integer":
        error = "Please enter an integer more than zero"
        change_to = int
    else:
        error = "please enter a number more than zero"
        change_to = float

    while True:
        response = input(question).lower()

        # check for exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's
            # more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    my_float = num_checker("Please enter a number more than 0: ", "float")
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = num_checker("Please enter an integer more than 0: ", "integer", "")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")