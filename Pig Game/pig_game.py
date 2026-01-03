print("Pig Game")

import random

def roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (2 - 4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid input, try again.")

print("Number of players:", players)

max_score = 50
players_scores = [0 for _ in range(players)]

# Main game loop
while max(players_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has started!")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ")

            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled:", value)
                print("Current score:", current_score)

        players_scores[player_idx] += current_score
        print("Total score:", players_scores[player_idx])

# Winner
winner = players_scores.index(max(players_scores)) + 1
print(f"\nPlayer {winner} wins with {max(players_scores)} points!")


