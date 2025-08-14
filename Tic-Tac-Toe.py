import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-"*5)

def check_winner(player):
    win_patterns = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_patterns)

def play():
    while True:
        print_board()
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move!")
            continue
        board[move] = "X"
        if check_winner("X"):
            print_board()
            print("You win!")
            break
        if " " not in board:
            print_board()
            print("It's a tie!")
            break
        comp_move = random.choice([i for i, spot in enumerate(board) if spot == " "])
        board[comp_move] = "O"
        if check_winner("O"):
            print_board()
            print("Computer wins!")
            break

if __name__ == "__main__":
    play()
