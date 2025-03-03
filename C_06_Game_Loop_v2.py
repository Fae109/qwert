import random


def initial_points(which_player):
    """Roll dice twice and return roll / if double points apply"""

    double = "no"

    # roll dice for user note if they got double (to change die, change the 6s to the die you want e.g. D4 ,D6. D8,
    # D10, 12, D20, ETC.
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double


def make_statement(statement, deceration):
    """adds emoji / additional characters to the start amd end of headings"""

    ends = deceration * 3
    print(f"{ends} {statement} {ends}")

# Main routine starts here



# at start of game the comp / user score are both 0
comp_score = 0
user_score = 0

game_goal = int(input("game goal: "))

# play multible rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # start of round loop
    # For testing purposes, ask the user what the points for the user / comp were

    # roll the dice for user note if they got a double
    initial_user = initial_points("user")
    initial_comp = initial_points("comp")

    # Retrieve user and computer points from content returned by function
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # let user know if they qualify for double points
    if double_user == "yes":
        print()
        print("Great news - If you win, you will get double points")

    # assume user goes 1st
    first = "user"
    second = "computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less then the computer\n")

    # if user and comps rolls are the same. user is player 1...
    elif user_points == comp_points:
        print("the initial rolls were the same, the user starts")

    # if comp has fewer points switch the comp to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # loop until we have winner
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round")
        print()

        # first person rolls the dice and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: rolled a {player_1_roll} - has {player_1_points} points")

        # if first person score is over 13 end round
        if player_1_points >= 13:
            break

        # second player rolls the dice and score is updated
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"\n{second}: rolled a {player_2_roll} - has {player_2_points} points")

    # print("end of round")

    #
    user_points = player_1_points
    comp_points = player_2_points

    #
    if first == "computer":
        user_points, comp_points = comp_points, user_points

    # work out who wom
    if user_points > comp_points:
        winner = "user"
    else:
        winner = "computer"

    # double user points of eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # output round results
    make_statement("round results", "=")
    round_feedback = f"user points: {user_points} | computer points: {comp_points}"
    round_feedback = f"the {winner} won."
    print(round_feedback)
    print()

    # outside rounds loop - update score with round points, only add points to the score op the
    comp_score += comp_points
    user_score += user_points

    # show ovrall scores (add this to round loops)
    print("*** game update ***")
    print(f"user score: {user_score} | comp score: {comp_score}")

# end game out put results
print()
if user_score > comp_score:
    print("the user won")
else:
    print("the comp won")
