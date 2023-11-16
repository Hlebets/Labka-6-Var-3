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
            print(
                f"Герой отримує {damage} одиниць шкоди та його здоров'я складає {self.health} одиниць"
            )

    def show_stats(self):
        print(
            f"Герой має {self.health} одиниць здоров'я та {self.damage} одиниць шкоди"
        )


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        else:
            print(
                f"\n Ворог отримує {damage} одиниць шкоди та його здоров'я складає {self.health} одиниць"
            )


class NothingEvent:
    def __init__(self):
        self.description = "\nНічого особливого чи визначного не сталося"
        self.location = ["Тим часом ви відвідали ліс", "Тим часом ви відвідали печеру"]

    def interact(self):
        print(self.description)
        print(random.choice(self.location))


class FortuneTellerEvent:
    def __init__(self):
        self.description = "Ви зустріли віщуна"
        self.phrase = [
            "Ви будете багатим",
            "Ви будете бідним",
            "Ви будете щасливі",
            "Ви будете сумні",
        ]

    def interact(self):
        print(self.description)
        print(random.choice(self.phrase))


class BattleEvent:
    def __init__(self, hero):
        self.description = "Ви зустріли ворога"
        self.hero = hero

    def interact(self):
        print(self.description)
        enemy = Enemy(random.randint(5, 10), random.randint(2, 5))
        while True:
            if self.hero.health <= 0:
                print("Гру завершено. Герой загинув. \nПовернення до головного меню...")
                delete_save()
                break
            print("\n1. Битися")
            print("2. Втікти")
            print("3. Відкрити статистику")
            action_input = input("Введіть значення для вибору дії: ")

            if action_input == "1":
                enemy.take_damage(random.randint(0, self.hero.damage))
                self.hero.take_damage(random.randint(0, enemy.damage))
                if enemy.health <= 0:
                    print("Ворога переможено!")
                    break
            elif action_input == "2":
                print("Ви втікли")
                break
            elif action_input == "3":
                print("Статистика героя:")
                self.hero.show_stats()
            else:
                print("Неправильний вибір. Будь ласка, введіть 1, 2 або q")


def game_loop(hero, completed_events):
    while True:
        print("1. Піти кудись")
        print("2. Відкрити статистику")
        print("3. Зберегти гру та повернутися до головного меню")
        action_input = input("Введіть значення для вибору дії: ")
        event = None
        if action_input == "1":
            print("Ви пішли у невідомому напрямку")
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
            print("\nВи відкрили статистику")
            hero.show_stats()
            print(f"Ви пройшли {completed_events} подій")

        elif action_input == "3":
            print("\nЗбереження гри...")
            save_game(hero, completed_events)
            break

        else:
            print("Неправильний вибір. Будь ласка, введіть 1, 2 або q")


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
