
import games

import os
FILE = os.path.join(os.path.dirname(__file__), "test2.txt")
game_library = {}

def save_games():
    with open(FILE, "w") as file:
        for game,rating in game_library.items():
            file.write(f"{game},{rating}\n")

def load_games():
    with open(FILE) as file:
        for line in file:
            if line.strip():
                game, rating = line.strip().split(",")
                game_library[game] = int(rating)

    return game_library

    