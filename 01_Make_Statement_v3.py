# functions go here
def make_statement(statement, decoration, lines=1):
    """Emphasises headings by adding decoration
    at the start and end"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes here
make_statement("Greetings", "=", 3)
print()
make_statement("Hello", "#", 2)
print()
make_statement("Salutations", "👍")
print()