
# function go here

def yes_no(question):

    """checks user response to a question is yes/ no(y/n), returns 'yes' or 'no'"""
    while True:

        response = input(question).lower()

        # check the user says yes/no
        if response == "yes" or response == "y":
            return"yes"

        elif response == "no" or response == "n":
             return"no"
        else:
            print("please enter yes/no")


# Main routine

want_instructions = yes_no("Do you want to see the instructions? ")
want_coffe =yes_no("Do you want coffe? ")
print("we done")


