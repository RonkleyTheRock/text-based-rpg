while True:
    print("===================================")
    print("   SUPER AWESOME GAME FOR          ")
    print("        AWESOME PEOPLE             ")
    print("===================================")
    print()
    print("1. Play")
    print("2. Exit")

    player_choice = input("Choose an option: ")

    if player_choice == "1":
        print()
        print("Select Difficulty")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")

        difficulty = input("Choose a difficulty: ")

        if difficulty == "1":
            difficulty_multiplier = 0.75
            print("Easy difficulty selected!")

        elif difficulty == "2":
            difficulty_multiplier = 1.0
            print("Normal difficulty selected!")

        elif difficulty == "3":
            difficulty_multiplier = 1.5
            print("Hard difficulty selected!")

        else:
            print("Invalid option.")
            continue

        print("Starting game...")
        break

    elif player_choice == "2":
        print("Thanks for playing!")
        break

    else:
        print("Invalid option. Please choose 1 or 2.")
