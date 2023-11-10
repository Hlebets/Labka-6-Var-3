import random
import json


class Hero:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("Hero is dead")
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
            print("Enemy is defeated")
        else:
            print(f"Enemy takes {damage} damage and has {self.health} HP left.")

class NothingEvent:
    def __init__(self):
        self.description = "Nothing special happened during this trip"
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
    def __init__(self):
        self.description = "You have met an enemy"

    def interact(self):
        print(self.description)
        enemy = Enemy(random.randint(5, 10), random.randint(2, 5))
        hero = Hero(20, 7)
        while True:
            print("1. Fight")
            print("2. Run")
            print("3. Open Stats")
            action_input = input("Enter your choice: ")

            if action_input == "1":
                hero.take_damage(random.randint(0, enemy.damage))
                enemy.take_damage(random.randint(0, hero.damage))
                if enemy.health <= 0:
                    print("Enemy defeated!")
                    break
            elif action_input == "2":
                print("You ran away.")
                break
            elif action_input == "3":
                print(
                    f"Hero stats: {hero.show_stats()}"
                )
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
