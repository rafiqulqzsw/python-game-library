games = {}
import os

FILE = os.path.join(os.path.dirname(__file__), "test.txt")

with open(FILE) as file:
    for line in file:
        if line.strip():
            game, rating = line.strip().split(",")
            games[game] = int(rating)

def save_games():
    with open(FILE, "w") as file:
        for game,rating in games.items():
            file.write(f"{game},{rating}\n")

def get_rating():
    while True:
        try:
            rating = int(input("Enter your rating!"))
            if rating in range(1,11):
                print("game added!")
                return rating
            else:
                print("Rating must be between 1 and 10")
                continue
        except ValueError:
            print("that wont work lad!")
            continue

def edit_rating():
    game = input("Enter your game")
    if game in games:
        rating = get_rating()
        games[game] = rating
        save_games()
    else:
        print("You dont have that game!")
        answer = input("Would you like to add it?")
        if answer == "no":
            print("Then no change will be made.")
        elif answer == "yes":
            rating = get_rating()
            games[game] = rating
            save_games()

def menu():
    print("1.Show all games")
    print("2.Add a game")
    print("3.Find a game")
    print("4.Remove a game")
    print("5.edit a rating")
    print("6.quit")

def show_games():
    for game, rating in games.items():
        print(game, rating)

def add_game():
    game = input("Enter your game")


    if game in games:
        return False
    else:
        rating = get_rating()
        games[game] = rating
        save_games()


        return True

def find_game():
    game = input("What game would you like to find")
    if game in games:
        return games[game]
    else:
        return None

def delete_game():
    game = input("Which game would you like to remove?")
    if game in games:
        del games[game]
        print(f"{game} deleted successfully!")
        save_games()


    else:
        print("that game isnt in your library")
    

while True:
    menu()

    number = 0
    try:
        number = int(input("enter"))
    except ValueError:
        print("that wont work lad!")


    if number == 1:
        show_games()

    elif number == 2:
        status = add_game()
        if status is True:
            print("Your game has been added!")
        elif status is False:
            print("This game already exists!")


    elif number == 3:
        rating = find_game()
        if rating is not None:
            print(f"Rating: {rating}")
        else:
            print("That game doesnt exist here")

    elif number == 4:
        delete_game()

    elif number == 5:
        edit_rating()

    elif number == 6:
        break
