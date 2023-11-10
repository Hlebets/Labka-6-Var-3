import random


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


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def take_damage(self, hero):
        hero.take_damage(self.damage)
