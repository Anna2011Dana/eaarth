import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    win_lines = [board[0], board[1], board[2],
                 [board[0][0], board[1][0], board[2][0]],
                 [board[0][1], board[1][1], board[2][1]],
                 [board[0][2], board[1][2], board[2][2]],
                 [board[0][0], board[1][1], board[2][2]],
                 [board[0][2], board[1][1], board[2][0]]]
    return [player, player, player] in win_lines

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def player_move(board):
    while True:
        try:
            move = int(input("Ваш хід (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Клітинка зайнята! Спробуйте ще раз.")
        except (ValueError, IndexError):
            print("Некоректний ввід! Введіть число від 1 до 9.")

def computer_move(board):
    row, col = random.choice(get_empty_cells(board))
    board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Вітаємо у грі Хрестики-нулики!")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            computer_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("Ви перемогли!")
            return
        elif check_winner(board, "O"):
            print("Комп'ютер переміг!")
            return

    print("Нічия!")

if __name__ == "__main__":
    main()
