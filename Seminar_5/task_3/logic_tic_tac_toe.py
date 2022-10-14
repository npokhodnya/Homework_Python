# Создайте программу для игры в ""Крестики-нолики"".
import random


def win(x_moves, o_moves):
    winners = ({1, 2, 3},
               {4, 5, 6},
               {7, 8, 9},
               {1, 4, 7},
               {2, 5, 8},
               {3, 6, 9},
               {1, 5, 9},
               {3, 5, 7})
    for i in winners:
        if x_moves & i == i:
            return "X"
        elif o_moves & i == i:
            return "O"
    return False


def is_valid_move(x_moves: set, o_moves: set, move: str):
    all_moves = x_moves | o_moves
    if not move.isdigit() or 10 < int(move) or int(move) < 1 or int(move) in all_moves:
        return False
    return True


def table(cur_table=None):
    table_ = \
        """ 
        1   2   3
        4   5   6
        7   8   9
        """ if cur_table is None else cur_table
    return table_


def change_table(table_, move, player):
    a = f"{player}"
    table_ = table_.replace(move, a)
    return table_


def player_move(o_moves: set, x_moves: set, player: str, table_=None):
    print(f"Ход игрока: {player}")
    print("~" * 25)
    print(f"Поле сейчас:")
    print(table(table_))
    move = input(f"Введите цифру, находящуюся в таблице, на которую хотите походить: ")
    m = is_valid_move(x_moves, o_moves, move)
    while not m:
        print("\n")
        print("\033[31mЭто число не подходит!!!!!\033[0m")
        print("\n")
        print(f"Ход игрока: {player}")
        print("~" * 25)
        print(f"Поле сейчас:")
        print(table(table_))
        move = input(f"Введите цифру, находящуюся в таблице, на которую хотите походить: ")
        m = is_valid_move(x_moves, o_moves, move)
    if player == "X":
        x_moves.add(int(move))
        return change_table(table_, move, player), x_moves, o_moves
    else:
        o_moves.add(int(move))
        return change_table(table_, move, player), x_moves, o_moves


def game():
    first_player, second_player = "X", "O"
    current_player = (first_player, second_player)[random.randint(0, 1)]
    x_moves = set()
    o_moves = set()
    table_ = table()
    count = 0
    while True:
        count+=1
        if not win(x_moves, o_moves):
            current_player = second_player if current_player == first_player else first_player
            table_, x_moves, o_moves = player_move(o_moves, x_moves, current_player, table_)
        else:
            break
        if count == 9:
            break
    print(table(table_))
    if count == 9:
        print(f"\033[33mНичья!\033[0m")
    else:
        print(f"\033[32mПобедитель - {current_player}\033[0m")
