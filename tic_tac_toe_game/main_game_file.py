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

        print_game_field()

        # Cycle for 1 party
        while not (win or lose):

            player_move = tuple(input('Input coordinates in x, y + ' +
                                      f'format(0-{FIELD_WIDTH - 1}): '))
            player_moves.append(player_move)

            print_game_field(player_moves, ai_moves)

            ai_move = make_ai_turn()
            ai_moves.append(ai_move)

            print_game_field(player_moves, ai_moves)

        print('Play another game? (Y/N):', end='')
        user_another = input().upper()
        if user_another == 'N':
            finished = True


def print_game_field(player_1, player_2):  # TODO print game field
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    raw = 0
    print('\t', 0, 1, 2)
    print('--------')
    for line in game:
        print(raw, '|', end='')
        print('\t', line)
        print('--------')
        raw += 1


def make_ai_turn(): #TODO ai turn
    pass


def count_points(): #TODO count points
    pass


# Start main function
main()
