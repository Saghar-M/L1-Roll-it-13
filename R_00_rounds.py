# cheks for na integer more than 0 (allows <enter>)

def int_check(question):
    while True:

        error = "please enter an integer that is 1 or more. "

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1
            if response <1:
                 print(error)
            else:
                return response


        except ValueError:
             print(error)


# main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0


print("💎📄✂️ Rock / Paper / Scissors Game 💎📄✂️")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode ="infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings ( based on mode)
    if mode == "infinite":
        rounds_heading = f"\n 💿💿💿 Round {rounds_played +1} (infinite Mode) 💿💿💿 "
    else:
        rounds_heading = f"f\n 💿💿💿 Round {rounds_played +1} of {num_rounds} 💿💿💿 "

    print(rounds_heading)
    print()

    user_choice =  input("Choose: ")

    # if user choose, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area