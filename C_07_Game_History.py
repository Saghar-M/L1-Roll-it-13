
# initialise list to hold game history
game_history =[]

# Get data (base component does this already, code below fore testing purpose)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User Points ? "))
    comp_points = int(input("Computer Points ? "))
    winner = input("who won? ")
    user_score = int(input("User score ? "))
    comp_score = int(input("Computer score ? "))

    game_results = (f"Round {rounds_played}: User points {user_points} | "
                    f"Computer points {comp_points}, {winner} wins "
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)