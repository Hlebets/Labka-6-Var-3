from classes import (
    Hero,
    game_loop,
    load_game,
)


while True:
    print("\nМаленький світ - Невеличка текстова гра")
    print("1. Нова Гра")
    print("2. Продовжити")
    print("q. Вихід")
    main_menu_input = input("Введіть значення для вибору дії: ")

    if main_menu_input == "1":
        print("\nНову гру розпочато!")
        completed_events = 0
        hero = Hero(health=20, damage=7)
        event = None
        game_loop(hero, completed_events)

    elif main_menu_input == "2":
        print("\n Продовження гри")
        try:
            load_game()
            hero, completed_events = load_game()
            game_loop(hero, completed_events)
        except Exception:
            print(
                "\nФайл збереження не було знайдено \nПовернення до головного меню... "
            )

    elif main_menu_input == "q":
        print("\nВихід")
        break

    else:
        print("Неправильний вибір. Будь ласка, введіть 1, 2 або q")
