from random import randint
from copy import deepcopy

# Number of passive turns to make
PASIVE_TURNS = 35

# Read board into 2d list
def read_board():
    board = []
    for i in range(10):
        board.append([int(x) for x in input().split()])
    return board

# Get Number of current turn
def num_turn():
    turns = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1 or board[i][j] == 2:
                turns += 1
    return turns + 1

# Print move and reason
def print_move(place, reason):
    print(place[0], place[1])
    print(reason)

# Get the value at the given coordinates
def get_piece(board, piece):
    return board[piece[0]][piece[1]]

# Check if piece is within boundaries. Returns True/False
def in_bounds(piece):
    if piece[0] >= 0 and piece[1] >= 0 and piece[0] <= 9 and piece[1] <= 9:
        return True
    else:
        return False

# Get a list of all valid moves (have 3 in place)
def valid_moves(board):
    valid = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                valid.append((i, j))
    return valid


# Take direction and turn into delta x/y
def dir_to_delta(direction):
    delta = {
        1: (-1, 0),  # UP
        2: (-1, 1),  # UP-RIGHT
        3: (0, 1),   # RIGHT
        4: (1, 1),   # DOWN-RIGHT
        5: (1, 0),   # DOWN
        6: (1, -1),  # DOWN-LEFT
        7: (0, -1),  # LEFT
        8: (-1, -1)  # UP-LEFT
    }

    return delta[direction]


# Check direction until empty space or own piece. Returns number of opponent pieces in path
def check_direction(board, start, player, direction):
    delta_y, delta_x = dir_to_delta(direction)

    current_piece = (start[0] + delta_y, start[1] + delta_x)
    opponent_pieces = 0

    # Loop until current piece is
    while in_bounds(current_piece) and get_piece(board, current_piece) != player and get_piece(board, current_piece) != 3 and get_piece(board, current_piece) != 0:
        opponent_pieces += 1
        current_piece = (current_piece[0] + delta_y, current_piece[1] + delta_x)
    else:
        # Reset score if doesnt end in player piece
        if not in_bounds(current_piece) or get_piece(board, current_piece) != player:
            opponent_pieces = 0

    return opponent_pieces

# Check direction until empty space or own piece. Returns number of opponent pieces in path
def check_direction_two(board, start, player, direction):
    delta_y, delta_x = dir_to_delta(direction)

    current_piece = (start[0] + delta_y, start[1] + delta_x)
    opponent_pieces = []

    # Loop until current piece is
    while in_bounds(current_piece) and get_piece(board, current_piece) != player and get_piece(board, current_piece) != 3 and get_piece(board, current_piece) != 0:
        opponent_pieces.append(current_piece)
        current_piece = (current_piece[0] + delta_y, current_piece[1] + delta_x)
    else:
        # Reset score if doesnt end in player piece
        if not in_bounds(current_piece) or get_piece(board, current_piece) != player:
            opponent_pieces = []

    return opponent_pieces

def check_open(board, start, player):
    opponent = 2 if player == 1 else 1

    pieces_to_replace = []
    tmp_board = deepcopy(board)

    for i in range(10):
        for j in range(10):
            if tmp_board[i][j] == 3:
                tmp_board[i][j] = 0

    for direction in range(1, 9):
        tmp_pieces = check_direction_two(board, start, player, direction)
        pieces_to_replace = pieces_to_replace + tmp_pieces

    for piece in pieces_to_replace:
        tmp_board[piece[0]][piece[1]] = player

    score = 0
    for direction in range(1, 5):
        delta_y, delta_x = dir_to_delta(direction)

        next_piece = (start[0] + delta_y, start[1] + delta_x)

        count = 0
        top_empty = False
        top_out = False

        while in_bounds(next_piece) and get_piece(tmp_board, next_piece) == player:
            if get_piece(board, next_piece) == opponent:
                count += 1
            next_piece = (next_piece[0] + delta_y, next_piece[1] + delta_x)
        else:
            if in_bounds(next_piece) and get_piece(tmp_board, next_piece) == 0:
                top_empty = True
            elif not in_bounds(next_piece):
                top_out = True

        next_piece = (start[0] - delta_y, start[1] - delta_x)

        bot_empty = False
        bot_out = False

        while in_bounds(next_piece) and get_piece(tmp_board, next_piece) == player:
            if get_piece(board, next_piece) == opponent:
                count += 1
            next_piece = (next_piece[0] - delta_y, next_piece[1] - delta_x)
        else:
            if in_bounds(next_piece) and get_piece(tmp_board, next_piece) == 0:
                bot_empty = True
            elif not in_bounds(next_piece):
                bot_out = True

        if bot_out or top_out or (bot_empty and top_empty) and count > 0:
            score += count
            #ret.append((direction, count, bot_out, top_out, bot_empty, top_empty))

    return score


# Check corners and make move if any
def check_corners(moves):
    corners = [(0,0), (0,9), (9,0), (9,9)]

    for move in moves:
        if move in corners:
            # Just return first corner for now
            return move

    return None

# Given a list of moves, remove pieces that set up corners
def remove_corner_setups(board, moves):
    new_moves = []

    setups = {
        (0,0): [(0,1), (1,0), (1,1)],
        (0,9): [(0,8), (1,9), (1,8)],
        (9,0): [(8,0), (8,1), (9,1)],
        (9,9): [(9,8), (8,8), (8,9)]
    }

    for move in moves:
        valid = True

        for key, value in setups.items():
            if move in value and get_piece(board, key) == 0:
                valid = False
        if valid:
            new_moves.append(move)

    return new_moves


def get_power_spots(board, moves):
    power_moves = {
        (0,0): [(0,2), (2,0)],
        (0,9): [(0,7), (2,9)],
        (9,0): [(7,0), (9,2)],
        (9,9): [(9,7), (7,9)]
    }

    available_power = []

    for corner, pm in power_moves.items():
        if get_piece(board, corner) == 0:
            for move in pm:
                available_power.append(move)

    available_moves = [x for x in moves if x in available_power]

    if len(available_moves) == 0:
        power_moves = {
            (0,0): [(2,2)],
            (0,9): [(2,7)],
            (9,0): [(7,2)],
            (9,9): [(7,7)]
        }

        for corner, pm in power_moves.items():
            if get_piece(board, corner) == 0:
                for move in pm:
                    available_power.append(move)

        available_moves = [x for x in moves if x in available_power]

    return available_moves


# Make a random move from a list of moves
def random_move(moves):
    x = randint(0, len(moves)-1)
    print_move(moves[x], "Random Move")

# Main logic, to make Move
def make_move(board, player):
    # Get points of all points
    moves = valid_moves(board)

    # Check for corners first
    corner = check_corners(moves)

    if corner is not None:
        print_move(corner, "Thankyou")
        return

    # Check power_moves
    power = get_power_spots(board, moves)

    if len(power) > 0:
        random_move(power)
        return

    # Remove setups from list of valid moves
    moves = remove_corner_setups(board, moves)

    if len(moves) == 0:
        moves = valid_moves(board)

    best_move = 0
    best_score = 0
    reason = ""

    if num_turn() <= PASIVE_TURNS:
        reason = "Passive"
        for i in range(len(moves)):
            cur_score = check_open(board, moves[i], player)
            if cur_score <= best_score:
                best_score = cur_score
                best_move = i
    else:
        reason = "Aggro"
        for i in range(len(moves)):
            cur_score = check_open(board, moves[i], player)
            if cur_score >= best_score:
                best_score = cur_score
                best_move = i

    print_move(moves[best_move], reason)

if __name__ == "__main__":
    board = read_board()
    player = int(input())

    make_move(board, player)
