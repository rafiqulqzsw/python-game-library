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

