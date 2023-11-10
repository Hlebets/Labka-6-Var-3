import random
from classes import NothingEvent, FortuneTellerEvent, BattleEvent, Hero, Enemy
import random

completed_events = 0
hero = Hero(random.randint(10, 20), random.randint(3, 5))

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
            action_input = input("Enter your choice: ")
            if action_input == "1":
                print("You are going in a chosen direction")
                event_type = random.choice(["Nothing", "FortuneTeller", "Battle"])
                event = None
                enemy = None
                if event_type == "Nothing":
                    event = NothingEvent()
                elif event_type == "FortuneTeller":
                    event = FortuneTellerEvent()
                elif event_type == "Battle":
                    event = BattleEvent()
                    enemy = Enemy(random.randint(10, 20), random.randint(3, 5))

                if event is not None:
                    event.interact()
                else:
                    ("Unexpected event type")
                completed_events += 1
                print("1. Fight")
                print("2. Run")
                print("3. Open Stats")
                input("Enter your choice: ")
                if action_input == "1":
                    print("You are fighting")
                elif action_input == "2":
                    print("You are running")
                    if enemy is not None:
                        print("Enemy is attacking")
                        print(
                            f"Hero received {enemy.damage} damage. {hero.health} HP left."
                        )
                elif action_input == "3":
                    hero.show_stats()
                else:
                    print("Invalid input, try again")
            elif action_input == "2":
                print("\nYou have opened stats")
                hero.show_stats()
                print(f"You have completed {completed_events} events")
    elif main_menu_input == "2":
        print("Continue")
    elif main_menu_input == "q":
        print("Exit")
        break
    else:
        print("Invalid input")
