
error = "Please enter an integer between 5-15"

while True:
    try:
        game_goal = int(input("What is the game goal? "))

        if game_goal < 5:
            print(error)
        elif game_goal > 15:
            print(error)
        else:
            print(f"Game goal: {game_goal}")
            break

    except ValueError:
        print(error)

