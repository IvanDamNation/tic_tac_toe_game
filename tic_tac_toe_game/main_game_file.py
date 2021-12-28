# This is a main file of "tic-tac-toe" game.
# Gameplay in Python Console only (for now)

# Made for final practice exercise in chapter
# "Introduction in Python" for SkillFactory

# For education purpose only. Workability is not guarantee.

# Made by IvanDamNation (a.k.a. IDN)
# GNU General Public License v3, 2021


import random  # for AI turns

# Options
FIELD_WIDTH = 3  # Game field columns and rows (default=3)
# In plans: make "FIELD_WIDTH" full changeable (Done)


def main():
    # Get rules
    print('Welcome to the "tik-tak-toe" game')
    print('Place your mark by entering x and y field coordinates.')
    print('Classical rules:')
    print(f'For win make {FIELD_WIDTH} column, row or diagonal')
    print('with your mark.')

    finished = False
    # points = [[], []]

    # Cycle for whole game
    while not finished:
        result = body_game_party()

        count_points(result)

        print('Play another game? (Y/N):', end='')
        user_another = input().upper()
        if user_another == 'N':
            finished = True


def body_game_party():
    # Starting condition
    party_result = None
    moves_count = 0
    player_moves = []
    ai_moves = []

    print_game_field(player_moves, ai_moves)

    # Cycle for party #
    while not party_result:
        # Player move
        player_moves.append(make_player_turn(player_moves, ai_moves))
        moves_count += 1
        # print(player_moves)  # Uncomment for check each turn
        check_condition = print_game_field(player_moves, ai_moves)

        if finish_game(check_condition):
            party_result = 'win'
            print('You win!')
            return party_result
        elif FIELD_WIDTH ** 2 == moves_count:
            party_result = 'tie'
            print('Tie.')
            return party_result

        input('Press "Enter" for AI turn.')

        # AI move
        ai_moves.append(make_ai_turn(player_moves, ai_moves))
        moves_count += 1
        # print(ai_moves)  # Uncomment for check each AI turn
        check_condition = print_game_field(player_moves, ai_moves)

        if finish_game(check_condition):
            party_result = 'lose'
            print('AI win.')
            return party_result
        elif FIELD_WIDTH ** 2 == moves_count:
            party_result = 'tie'
            print('Tie.')
            return party_result


def print_game_field(player_1, player_2):  # Done. Make documentation
    game = [[' '] * FIELD_WIDTH for line in range(FIELD_WIDTH)]

    for move in player_1:
        game[move[0]][move[1]] = 'x'
    for move in player_2:
        game[move[0]][move[1]] = 'o'

    print('\t', ' | '.join(map(str, range(FIELD_WIDTH))), end=' |\n')
    print('\t', '----' * FIELD_WIDTH, sep='')

    raw = 0
    for line in game:
        print(raw, ' | ', end='')
        print(' | '.join(map(str, line)), end=' |\n')
        print('\t', '----' * FIELD_WIDTH, sep='')
        raw += 1

    return game


def make_player_turn(player_1, player_2):  # Done. Make documentation
    new_player_move = None
    cheat = True
    while cheat:
        try:
            player_cor_x = int(input('Input coordinate in x ' +
                                     f'format(0-{FIELD_WIDTH - 1}): '))
            player_cor_y = int(input('Input coordinate in y ' +
                                     f'format(0-{FIELD_WIDTH - 1}): '))
            new_player_move = tuple([player_cor_y, player_cor_x])

            if new_player_move in set(player_1 + player_2):
                print('This place is filled already. Try another one.')
            elif player_cor_x < 0 or player_cor_x > FIELD_WIDTH:
                print('X coordinate is out of field.')
            elif player_cor_y < 0 or player_cor_y > FIELD_WIDTH:
                print('Y coordinate is out of field.')
            else:
                cheat = False
        except ValueError:
            print('Error! Check your input.')

    return new_player_move


def make_ai_turn(player_1, player_2):  # Done. Make documentation
    new_ai_move = None
    cheat = True
    while cheat:
        cor_x = random.randint(0, FIELD_WIDTH - 1)
        cor_y = random.randint(0, FIELD_WIDTH - 1)
        new_ai_move = (cor_x, cor_y)

        if new_ai_move not in set(player_1 + player_2):
            cheat = False

    return new_ai_move


# Make documentation
def finish_game(party):  # Remake this in future for full changeable (Done)
    # Horizontal check
    for line in range(FIELD_WIDTH):
        win_streak = []
        for col in range(FIELD_WIDTH):
            win_streak.append(party[line][col])
        if len(set(win_streak)) == 1 and ' ' not in win_streak:
            return True

    # Vertical check
    for line in range(FIELD_WIDTH):
        win_streak = []
        for col in range(FIELD_WIDTH):
            win_streak.append(party[col][line])
        if len(set(win_streak)) == 1 and ' ' not in win_streak:
            return True

    # Diagonal check #1
    win_streak = []
    for index in range(FIELD_WIDTH):
        win_streak.append(party[index][index])
    if len(set(win_streak)) == 1 and ' ' not in win_streak:
        return True

    # Diagonal check #2
    for index in range(FIELD_WIDTH):
        win_streak.append(party[index][FIELD_WIDTH - 1 - index])
    if len(set(win_streak)) == 1 and ' ' not in win_streak:
        return True

    return False


def count_points(party_ending):  # TODO count points
    pass


# Start main function
main()
