board = [' ' for _ in range(9)]
def insert(letter, pos):
    board[pos] = letter
def space_is_free(pos):
    return board[pos] == ' '
def print_board():
    row_1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row_2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row_3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print("\n" + row_1 + "\n" + row_2 + "\n" + row_3 + "\n")
def is_board_full():
    if board.count(' ') > 1:
        return False
    else:
        return True
def check_for_win():
    win_lines = [
        [0, 1, 2],  # Across the top
        [3, 4, 5],  # Across the middle
        [6, 7, 8],  # Across the bottom
        [0, 3, 6],  # Down the left side
        [1, 4, 7],  # Down the middle
        [2, 5, 8],  # Down the right side
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]

    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return True

    return False

def player_move(player):
    run = True
    while run:
        move = input("Player {0}, please select a position to place an '{0}' (1-9): ".format(player))
        try:
            move = int(move)
            if 1 <= move <= 9:
                if space_is_free(move-1):
                    run = False
                    insert(player, move-1)
                else:
                    print("This postion is already occupied!")
            else:
                print("Please type a number within the range!")
        except ValueError:
            print("Please type a number!")

def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while not is_board_full():
        if not check_for_win():
            player_move('O')
            print_board()
        else:
            print("X's won this time!")
            break

        if not is_board_full():
            if not check_for_win():
                player_move('X')
                print_board()
            else:
                print("O's won this time! ")
                break

    if is_board_full():
        if not check_for_win():
            print("Tie Game!")

if __name__ == "__main__":
    main()


