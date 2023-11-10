import random
from tkinter import N
from classes import (
    NothingEvent,
    FortuneTellerEvent,
    BattleEvent,
    Hero,
    Enemy,
    save_game,
    load_game,
)
import random
import json

hero = Hero(20, 7)
event = None
completed_events = 0

while True:
    print("Small World - A small text RPG game")
    print("1. Start New Game")
    print("2. Continue")
    print("q. Exit")
    main_menu_input = input("Enter your choice: ")

    if main_menu_input == "1":
        print("New Game starts now!")

        while True:
            print("1. Go Somewhere")
            print("2. Open Stats")
            print("3. Save game and return to main menu")
            action_input = input("Enter your choice: ")

            if action_input == "1":
                print("You are going in a chosen direction")
                event_type = random.choice(["Nothing", "FortuneTeller", "Battle"])
                if event_type == "Nothing":
                    event = NothingEvent()
                elif event_type == "FortuneTeller":
                    event = FortuneTellerEvent()
                elif event_type == "Battle":
                    event = BattleEvent()

                if event is not None:
                    event.interact()
                    completed_events += 1

            elif action_input == "2":
                print("\nYou have opened stats")
                hero.show_stats()
                print(f"You have completed {completed_events} events")

            elif action_input == "3":
                print("Saving game...")
                save_game(hero, completed_events)
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    elif main_menu_input == "2":
        print("Continue")
        load_game()

        while True:
            print("1. Go Somewhere")
            print("2. Open Stats")
            print("3. Save game and return to main menu")
            action_input = input("Enter your choice: ")

            if action_input == "1":
                print("You are going in a chosen direction")
                event_type = random.choice(["Nothing", "FortuneTeller", "Battle"])
                if event_type == "Nothing":
                    event = NothingEvent()
                elif event_type == "FortuneTeller":
                    event = FortuneTellerEvent()
                elif event_type == "Battle":
                    event = BattleEvent()

                if event is not None:
                    event.interact()
                    completed_events += 1

            elif action_input == "2":
                print("\nYou have opened stats")
                hero.show_stats()
                print(f"You have completed {completed_events} events")

            elif action_input == "3":
                print("Saving game...")
                save_game(hero, completed_events)
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    elif main_menu_input == "q":
        print("Exit")
        break

    else:
        print("Invalid input")
