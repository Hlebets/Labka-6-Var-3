from classes import (
    Hero,
    game_loop,
    load_game,
)

event = None
completed_events = 0

while True:
    print("\nSmall World - A small text RPG game")
    print("1. Start New Game")
    print("2. Continue")
    print("q. Exit")
    main_menu_input = input("Enter your choice: ")

    if main_menu_input == "1":
        print("\nNew Game starts now!")
        hero = Hero(health=20, damage=7)
        game_loop(hero, completed_events)

    elif main_menu_input == "2":
        print("\nContinue")
        try:
            load_game()
            hero, completed_events = load_game()
            game_loop(hero, completed_events)
        except Exception:
            print("\nNo save file found")

    elif main_menu_input == "q":
        print("\nExit")
        break

    else:
        print("Invalid input")
