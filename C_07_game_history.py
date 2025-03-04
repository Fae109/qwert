
#
game_history = []

# get data

while True:
    rounds_played = input("round? ")
    if rounds_played == "":
        break

    user_points = int(input("user points? "))
    comp_points = int(input("comp points? "))
    winner = input("who won? ")
    user_score = int(input("user score: "))
    comp_score = int(input("comp score: "))

    game_results = (f"Round {rounds_played}: user points: {user_points} | " \
                   f"comp points {comp_points}, {winner} wins (15 | 0)" \
                   f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("game history")

for item in game_history:
    print(item)
