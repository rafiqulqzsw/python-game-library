import storage
import games
game_library = storage.load_games()

def main():
    while True:
        games.menu()

        number = 0
        try:
            number = int(input("enter"))
        except ValueError:
            print("that wont work lad!")


        if number == 1:
            games.show_games(game_library)

        elif number == 2:
            status = games.add_game(game_library)
            if status is True:
                print("Your game has been added!")
            elif status is False:
                print("This game already exists!")


        elif number == 3:
            rating = games.find_game(game_library)
            if rating is not None:
                print(f"Rating: {rating}")
            else:
                print("That game doesnt exist here")

        elif number == 4:
            games.delete_game(game_library)

        elif number == 5:
            games.edit_rating(game_library)

        elif number == 6:
            break
    

if __name__ == "__main__":
    main()