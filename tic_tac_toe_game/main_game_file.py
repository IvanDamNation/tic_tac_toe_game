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
    print('Place your mark by entering x and y field coords.')
    print(f'For win make {WIN_COUNT} column, row or diagonal')
    print('with your mark.')

    finished = False

    # Cycle for whole game
    while not finished:
        win = False
        lose = False
        player_moves = []
        ai_moves = []

        print_game_field(player_moves, ai_moves)

        # Cycle for 1 party
        while not (win or lose):
            player_moves.append(make_player_turn())
            # print(player_moves)  # Uncomment for check each turn

            print_game_field(player_moves, ai_moves)

            input('Press "Enter" for AI turn.')

            ai_moves.append(make_ai_turn())
            # print(ai_moves)  # Uncomment for check each AI turn
            print_game_field(player_moves, ai_moves)

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


def make_player_turn():  # Done. Make documentation
    player_cor_x = int(input('Input coordinate in x ' +
                             f'format(0-{FIELD_WIDTH - 1}): '))
    player_cor_y = int(input('Input coordinate in y' +
                             f'format(0-{FIELD_WIDTH - 1}): '))
    new_player_move = tuple([player_cor_x, player_cor_y])

    return new_player_move


def make_ai_turn():  # Done. Make documentation
    cor_x = random.randint(0, FIELD_WIDTH)
    cor_y = random.randint(0, FIELD_WIDTH)
    new_ai_move = (cor_x, cor_y)
    return new_ai_move


def count_points():  # TODO count points
    pass


# Start main function
main()
