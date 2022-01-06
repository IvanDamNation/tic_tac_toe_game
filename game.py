# This is a main file of "tic-tac-toe" game.
# Gameplay in Python Console only (for now).
# 'AI' is primitive (just random)

# Made for final practice exercise in chapter
# "Introduction in Python" for SkillFactory

# For education purpose only. Workability is not guarantee.

# Made by IvanDamNation (a.k.a. IDN)
# GNU General Public License v3, 2021


import random  # for AI turns
from options import *

def rules():
    return f'''
            Welcome to the "tic-tac-toe" game!\n
            Place your mark by entering x and y field coordinates.\n
            Classical rules:\n
            For win make {FIELD_WIDTH} column, row or diagonal'\n
            with your mark.
            '''


def game_party():
    """
    Sub-main function for one round. Controlling turns and determines
    the winner. Calls function of field printing.
    :return: result of the round (win, lose or tie)
    """

    # Starting condition
    party_result = None
    moves_count = 0
    player_moves = []
    ai_moves = []

    game_field(player_moves, ai_moves)

    # Cycle for party
    while not party_result:
        moves_count += 1

        if moves_count % 2 != 0:
            # Player move
            player_moves.append(make_turn(player_moves, ai_moves))
            # print(ai_moves)  # Uncomment for check each player turn
        elif moves_count % 2 == 0:
            input('Press "Enter" for AI turn.')
            # AI move
            ai_moves.append(make_ai_turn(player_moves, ai_moves))
            # print(ai_moves)  # Uncomment for check each AI turn

        check_condition = game_field(player_moves, ai_moves)

        if finish_game(check_condition) and moves_count % 2 != 0:
            party_result = 'win'
            print('You win!')
            return party_result
        elif finish_game(check_condition):
            party_result = 'lose'
            print('AI win.')
            return party_result
        elif moves_count == FIELD_WIDTH ** 2:
            party_result = 'tie'
            print('Tie.')
            return party_result


def game_field(player_1: list, player_2: list):
    """
    Prints visualized form of round statement, based on move logs.
    :param player_1: Log of Player moves
    :param player_2: Log of AI moves
    :return: 'game field'-list
    """

    game = [[' '] * FIELD_WIDTH for _ in range(FIELD_WIDTH)]

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


def make_turn(player_1: list, player_2: list):
    """
    Gets coordinates from player for new move. Have primitive
    anti-cheat and fool-protection.
    :param player_1: Log of Player moves
    :param player_2: Log of AI moves
    :return: Coordinates of new Player mark
    """

    new_player_move = None
    cheat = True
    while cheat:
        try:
            player_cor_x = int(input('Input coordinate in x ' +
                                     f'format(0-{FIELD_WIDTH - 1}): '))
            player_cor_y = int(input('Input coordinate in y ' +
                                     f'format(0-{FIELD_WIDTH - 1}): '))
            new_player_move = (player_cor_y, player_cor_x)

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


def make_ai_turn(player_1: list, player_2: list):
    """
    Make AI get coordinates for new move. Have 'same move'-protection.
    :param player_1: Log of Player moves
    :param player_2: Log of AI moves
    :return: Coordinates of new AI mark
    """

    new_ai_move = None
    cheat = True
    while cheat:
        cor_x = random.randint(0, FIELD_WIDTH - 1)
        cor_y = random.randint(0, FIELD_WIDTH - 1)
        new_ai_move = (cor_x, cor_y)

        if new_ai_move not in set(player_1 + player_2):
            cheat = False

    return new_ai_move


def finish_game(party: list):
    """
    Function trying to find 'win combination' and stops the round
    prematurely.
    :param party: 'game field'-list
    :return: True or False
    """
    # TODO: рефакторить повторяющийся код
    
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
    win_streak = []
    for index in range(FIELD_WIDTH):
        win_streak.append(party[index][-1 - index])
    if len(set(win_streak)) == 1 and ' ' not in win_streak:
        return True

    return False


def count_points(party_ending: str, points: list):
    """
    Giving 1 point to winner of this round.
    :param party_ending: result of game round
    :param points: score counter from previous rounds
    :return: renewed score counter
    """
    if party_ending == 'win':
        points[0] += 1
    elif party_ending == 'lose':
        points[1] += 1
    return points


if __name__ == '__main__':
    print(rules())

    finished = False
    score = [0, 0]

    # Cycle for whole game
    while not finished:
        result = game_party()

        score = count_points(result, score)

        print('Score (Player-AI):', score[0], '-', score[1])

        print('Play another game? (Y/N):', end='')
        user_another = input().upper()
        if user_another != 'Y':
            finished = True
