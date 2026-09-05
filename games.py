import storage
import validation

def menu():
    print("1.Show all games")
    print("2.Add a game")
    print("3.Find a game")
    print("4.Remove a game")
    print("5.edit a rating")
    print("6.quit")

def show_games(game_library):
    for game, rating in game_library.items():
        print(game, rating)

def add_game(game_library):
    game = input("Enter your game")


    if game in game_library:
        return False
    else:
        rating = validation.get_rating()
        game_library[game] = rating
        storage.save_games()


        return True

def find_game(game_library):
    game = input("What game would you like to find")
    if game in game_library:
        return game_library[game]
    else:
        return None

def edit_rating(game_library):
    game = input("Enter your game")
    if game in game_library:
        rating = validation.get_rating()
        game_library[game] = rating
        storage.save_games()
    else:
        print("You dont have that game!")
        answer = input("Would you like to add it?")
        if answer == "no":
            print("Then no change will be made.")
        elif answer == "yes":
            rating = validation.get_rating()
            game_library[game] = rating
            storage.save_games()

def delete_game(game_library):
    game = input("Which game would you like to remove?")
    if game in game_library:
        del game_library[game]
        print(f"{game} deleted successfully!")
        storage.save_games()


    else:
        print("that game isnt in your library")