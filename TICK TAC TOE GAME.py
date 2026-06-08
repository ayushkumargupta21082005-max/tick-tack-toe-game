board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board():
    for row in board:
        print(row[0], "|", row[1], "|", row[2])
        print("-" * 9)

def check_winner(player):

    # SIDE-SIDE WALA row
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # UPER NICHE WALA col
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Diagonals CROSS KE LIYE
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_draw():
    for row in board:
        if ' ' in row:
            return False
    return True

player = 'X'

while True:

    display_board()

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == ' ':

        board[row][col] = player

        if check_winner(player):
            display_board()
            print("Player", player, "wins!")
            break

        if is_draw():
            display_board()
            print("Match Draw!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    else:
        print("Invalid Move! Try Again.")