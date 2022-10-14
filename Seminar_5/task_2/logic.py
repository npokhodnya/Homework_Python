"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота "интеллектом"
"""
import random


def player_move(max_per_move: int, current_count: int, player: str):
    print(f"Ход игрока: {player}")
    print("~" * 25)
    max_ = current_count if max_per_move > current_count else max_per_move
    print(f"Сейчас: {current_count} конфет")
    move = input(f"Введите количество конфет, которые вы хотите взять (максимум - {max_}): ")
    if not move.isdigit() or max_ < int(move) or 1 > int(move):
        print("\n")
        print("\033[31mЭто число не подходит!!!!!\033[0m")
        print("\n")
        move = player_move(max_per_move, current_count, player)
    return int(move)


def bot_move(max_per_move: int, current_count: int):
    print(f"Ход Бота Фёдора")
    print("~" * 25)
    print(f"Сейчас: {current_count} конфет")
    move = current_count % (max_per_move + 1)
    if move == 0:
        move += 1
    print(f"Бот взял: {move} конфет")
    return move


def register(pvp: bool = True):
    if pvp:
        first = input("Выберите имя первого игрока: ")
        second = input("Выберите имя второго игрока: ")
        print("\n")
        return first, second
    else:
        first = input("Выберите имя игрока: ")
        print("\n")
        return first, "Бот Фёдор"


def settings():
    print("~" * 25)
    while True:
        max_ = input(f"Введите количество конфет: ")
        if not max_.isdigit():
            print("~" * 25)
            print("\033[31mЭто не число!!!\033[0m\n")
            continue
        max_count = input(f"Введите максимальное количество конфет, которое можно взять за один ход: ")
        if not max_count.isdigit() or int(max_count) > int(max_):
            print("~" * 25)
            print("\033[31mЭто число не подходит!!!\033[0m\n")
            continue
        return int(max_), int(max_count)


def mode():
    mode_ = input('0 - Игрок VS Бот Фёдор\n1 - Игрок VS Игрок\nВыберите режим: ')
    if not mode_.isdigit() or int(mode_) > 1 or int(mode_) < 0:
        print("\033[31mНеккоректный ввод!!!\033[0m\n")
        mode_ = mode()
    return int(mode_)


def game():
    mode_ = mode()
    max_, max_cnt = settings()
    first_player, second_player = register() if mode_ else register(False)
    current_player = (first_player, second_player)[random.randint(0, 1)]
    while max_ != 0:
        current_player = second_player if current_player == first_player else first_player
        move = player_move(max_cnt, max_, current_player) if current_player != "Бот Фёдор" else bot_move(max_cnt, max_)
        max_ -= move
        print(f"Осталось: {max_}\n")
    print(f"\033[32mПобедитель - {current_player}\033[0m")
