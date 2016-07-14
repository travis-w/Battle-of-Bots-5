from random import randint

# Read board into 2d list
def read_board():
    board = []
    for i in range(10):
        board.append([int(x) for x in input().split()])
    return board

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

# Check direction until empty space or own piece. Returns number of opponent pieces in path
def check_direction(board, start, player, direction):
    if direction == 1:
        # UP
        delta_y = -1
        delta_x = 0
    elif direction == 2:
        # UP-RIGHT
        delta_y = -1
        delta_x = 1
    elif direction == 3:
        # RIGHT
        delta_y = 0
        delta_x = 1
    elif direction == 4:
        # DOWN-RIGHT
        delta_y = 1
        delta_x = 1
    elif direction == 5:
        # DOWN
        delta_y = 1
        delta_x = 0
    elif direction == 6:
        # DOWN-LEFT
        delta_y = 1
        delta_x = -1
    elif direction == 7:
        # LEFT
        delta_y = 0
        delta_x = -1
    elif direction == 8:
        # UP-LEFT
        delta_y = -1
        delta_x = -1

    current_piece = (start[0] + delta_y, start[1] + delta_x)
    opponent_pieces = 0

    # Loop until current piece is
    while in_bounds(current_piece) and get_piece(board, current_piece) != player and get_piece(board, current_piece) != 3 and get_piece(board, current_piece) != 0:
        opponent_pieces += 1
        current_piece = (current_piece[0] + delta_y, current_piece[1] + delta_x)
    else:
        # Reset score if doesnt end in player piece
        if not in_bounds(current_piece) or get_piece(board, current_piece) != 1:
            opponent_pieces = 0

    return opponent_pieces


# Make a random move from a list of moves
def random_move(moves):
    x = randint(0, len(moves)-1)
    print_move(moves[x], "Random Move")

# Main logic, to make Move
def make_move(board, player):
    # Get points of all points
    moves = valid_moves(board)
    best_move = 0
    best_score = 0

    for i in range(len(moves)):
        cur_score = 0
        for direction in range(1,9):
            cur_score += check_direction(board, moves[i], player, direction)
        if cur_score >= best_score:
            best_score = cur_score
            best_move = i

    print_move(moves[best_move], "Best Score")

if __name__ == "__main__":
    board = read_board()
    player = int(input())

    make_move(board, player)
