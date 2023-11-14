import random
import json

filename = "savegame.json"


class Hero:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        else:
            print(f"Hero takes {damage} damage and has {self.health} HP left.")

    def show_stats(self):
        print(f"Hero has {self.health} health and {self.damage} damage.")


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        else:
            print(f"\nEnemy takes {damage} damage and has {self.health} HP left.")


class NothingEvent:
    def __init__(self):
        self.description = "\nNothing special happened during this trip"
        self.location = ["You have visited a forest", "You have visited a cave"]

    def interact(self):
        print(self.description)
        print(random.choice(self.location))


class FortuneTellerEvent:
    def __init__(self):
        self.description = "You met a fortune teller"
        self.phrase = [
            "You will be rich",
            "You will be poor",
            "You will be happy",
            "You will be sad",
        ]

    def interact(self):
        print(self.description)
        print(random.choice(self.phrase))


class BattleEvent:
    def __init__(self, hero):
        self.description = "You have met an enemy"
        self.hero = hero

    def interact(self):
        print(self.description)
        enemy = Enemy(random.randint(5, 10), random.randint(2, 5))
        while True:
            if self.hero.health <= 0:
                print("Game over, hero is dead. \nReturning to main menu...")
                delete_save()
                break
            print("\n1. Fight")
            print("2. Run")
            print("3. Open Stats")
            action_input = input("Enter your choice: ")

            if action_input == "1":
                enemy.take_damage(random.randint(0, self.hero.damage))
                self.hero.take_damage(random.randint(0, enemy.damage))
                if enemy.health <= 0:
                    print("Enemy defeated!")
                    break
            elif action_input == "2":
                print("You ran away.")
                break
            elif action_input == "3":
                print("Hero stats:")
                self.hero.show_stats()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


def game_loop(hero, completed_events):
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
                event = BattleEvent(hero)

            if event is not None:
                event.interact()
                completed_events += 1
            if hero.health <= 0:
                delete_save()
                break

        elif action_input == "2":
            print("\nYou have opened stats")
            hero.show_stats()
            print(f"You have completed {completed_events} events")

        elif action_input == "3":
            print("\nSaving game...")
            save_game(hero, completed_events)
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def save_game(hero, completed_events):
    game_state = {"hero": hero.__dict__, "completed_events": completed_events}
    with open("savegame.json", "w") as save_file:
        json.dump(game_state, save_file)


def load_game():
    with open("savegame.json", "r") as save_file:
        game_state = json.load(save_file)
        hero = Hero(**game_state["hero"])
        completed_events = game_state["completed_events"]
        return hero, completed_events


def delete_save():
    with open("savegame.json", "w") as save_file:
        save_file.write("")
