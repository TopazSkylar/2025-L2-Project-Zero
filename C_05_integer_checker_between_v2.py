def num_checker(question, low, high):
    """Checks users enter an integer between two values)"""

    error = f"Please enter an integer between {low} and {high}"

    while True:

        try:
            # Change the response to an integer and check that it's
            # more than zero
            response =int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    # ask user for an integer
    my_num = num_checker("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")