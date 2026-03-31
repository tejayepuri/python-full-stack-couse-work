import random

def dice():
    return random.randint(1, 6)

player_1 = input("Enter the player-1: ")
player_2 = input("Enter the player-2: ")

player1_score, player2_score = 0, 0
winning_point = 100

ladders = {6: 25, 12: 31, 35: 90, 46: 60, 51: 74, 78: 99, 82: 96}
snakes = {24: 5, 45: 18, 66: 33, 74: 37, 88: 77, 93: 57, 98: 21}

while player1_score < winning_point and player2_score < winning_point:

    
    status1 = input(f"{player_1}: [p]lay or [q]uit: ").lower()
    if status1 == 'p':
        dice_1 = dice()
        print(f"{player_1} Dice score: {dice_1}")
        player1_score += dice_1

        if player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f"+++++++ Ladder! New Score: {player1_score}")
        elif player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f"------- Snake Bite! New Score: {player1_score}")
        else:
            print(f"Board Score: {player1_score}")

    elif status1 == 'q':
        print(f"********** {player_2} won the game")
        break
    else:
        print("Enter valid input")

    
    status2 = input(f"{player_2}: [p]lay or [q]uit: ").lower()
    if status2 == 'p':
        dice_2 = dice()
        print(f"{player_2} Dice score: {dice_2}")
        player2_score += dice_2

        if player2_score in ladders:
            player2_score = ladders[player2_score]
            print(f"+++++++ Ladder! New Score: {player2_score}")
        elif player2_score in snakes:
            player2_score = snakes[player2_score]
            print(f"------- Snake Bite! New Score: {player2_score}")
        else:
            print(f"Board Score: {player2_score}")

    elif status2 == 'q':
        print(f"********** {player_1} won the game")
        break
    else:
        print("Enter valid input")

    
if player1_score >= winning_point:
    print(f"🏆 {player_1} won the game!")
elif player2_score >= winning_point:
    print(f"🏆 {player_2} won the game!")
