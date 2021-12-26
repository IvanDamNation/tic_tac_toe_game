# This is a main file of "tic-tac-toe" game.
# Gameplay in Python Console only (for now)

# Made for final practice exercise in chapter
# "Introduction in Python" for SkillFactory

# For education purpose only. Workability is not guarantee.

# Made by IvanDamNation (a.k.a. IDN)
# GNU General Public License v3.0


import random  # for AI turns

# Options
FIELD_WIDTH = 3  # Game field columns and rows (default=3)
WIN_COUNT = 3  # How much same symbols need for win (default=3)
# In plans: make "FIELD_WIDTH" changeable


def main():
    # Get rules
    print('Place your mark by entering x and y field coordinates.')
    print(f'For win make {WIN_COUNT} column, row or diagonal')
    print('with your mark.')

    finished = False

    # Cycle for whole game
    while not finished:
        win = False
        lose = False
        tie = False
        moves_count = 0
        player_moves = []
        ai_moves = []

        print_game_field(player_moves, ai_moves)

        # Cycle for 1 party # TODO replace to separate func
        while not (win or lose or tie):
            # Player move
            player_moves.append(make_player_turn(player_moves, ai_moves))
            moves_count += 1
            # print(player_moves)  # Uncomment for check each turn

            check_condition = print_game_field(player_moves, ai_moves)

            if finish_game(check_condition):
                win = True
            elif FIELD_WIDTH**2 == moves_count:
                tie = True

            input('Press "Enter" for AI turn.')

            # AI move
            ai_moves.append(make_ai_turn(player_moves, ai_moves))
            moves_count += 1
            # print(ai_moves)  # Uncomment for check each AI turn
            check_condition = print_game_field(player_moves, ai_moves)

            if finish_game(check_condition):
                lose = True
            elif FIELD_WIDTH**2 == moves_count:
                tie = True

        print('Play another game? (Y/N):', end='')
        user_another = input().upper()
        if user_another == 'N':
            finished = True


def print_game_field(player_1, player_2):  # Done. Make documentation
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    for move in player_1:
        game[move[0]][move[1]] = 'x'
    for move in player_2:
        game[move[0]][move[1]] = 'o'

    print('\t', 0, '|', 1, '|', 2)
    print('\t', '----------')

    raw = 0
    for line in game:
        print(raw, '|', end='')
        print('\t', line[0], '|', line[1], '|', line[2])
        print('\t', '----------')
        raw += 1

    return game


def make_player_turn(player_1, player_2):  # Done. Make documentation
    cheat = True
    while cheat:
        player_cor_x = int(input('Input coordinate in x ' +
                                 f'format(0-{FIELD_WIDTH - 1}): '))
        player_cor_y = int(input('Input coordinate in y ' +
                                 f'format(0-{FIELD_WIDTH - 1}): '))
        new_player_move = tuple([player_cor_x, player_cor_y])

        if new_player_move not in set(player_1 + player_2):
            cheat = False
        else:
            print('This place is filled already. Try another one.')

    return new_player_move


def make_ai_turn(player_1, player_2):  # Done. Make documentation
    cheat = True
    while cheat:
        cor_x = random.randint(0, FIELD_WIDTH - 1)
        cor_y = random.randint(0, FIELD_WIDTH - 1)
        new_ai_move = (cor_x, cor_y)

        if new_ai_move not in set(player_1 + player_2):
            cheat = False

    return new_ai_move


def finish_game(party_statement): # Remake this in future for full changeable
    # Horizontal check
    for line in party_statement:
        if all(line):
            return True

    # Vertical check

    # Diagonal check
    if (party_statement[0][0] ==
            party_statement[1][1] ==
            party_statement[2][2]) or \
            (party_statement[0][2] ==
             party_statement[1][1] ==
             party_statement[2][0]):
        return True


def count_points():  # TODO count points
    pass


# Start main function
main()
