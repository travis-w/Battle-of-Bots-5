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

# Get a list of all valid moves (have 3 in place)
def valid_moves(board):
    valid = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                valid.append((i, j))
    return valid

# Make a random move from a list of moves
def random_move(moves):
    x = randint(0, len(moves)-1)
    print_move(moves[x], "Random Move")


if __name__ == "__main__":
    board = read_board()
    player = int(input())

    random_move(valid_moves(board))
