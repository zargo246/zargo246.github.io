board = [" "," "," "," "," "," "," "," "," "," "]

def draw_board(board):
    print(board[7] + " |" + board[8] + " |" + board[9])
    print("--+--+--")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--+--+--")
    print(board[1] + " |" + board[2] + " |" + board[3])

player1 = input("Enter 1st Player name: ")
player2 = input("Enter 2nd Player name: ")

print(player1 + ": X |" + player2 + ": O")

def game():
    turn = "X" 
    count = 0
    player_turn = player1 
    
    for i in range(10): 
        draw_board(board)
        print("It's your turn, " + player_turn + ". Move to which place?")
        move = eval(input())

        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("That place is already filled. \nMove to which place?")
            continue

        if turn == "X":
            turn = "O"
            player_turn = player2   
        else: 
            turn = "X"
            player_turn = player1

        if count >= 5:
            if board [7] == board[8] == board[9] != " ": 
                declare_winner(turn)
                break
                
            elif board [4] == board[5] == board[6] != " ": 
                declare_winner(turn)
                break
                
            elif board [1] == board[2] == board[3] != " ": 
                declare_winner(turn)
                break
                
            elif board [1] == board[4] == board[7] != " ": 
                declare_winner(turn)
                break
                
            elif board [2] == board[5] == board[8] != " ": 
                declare_winner(turn)
                break
                
            elif board [3] == board[6] == board[9] != " ": 
                declare_winner(turn)
                break
            
            elif board [7] == board[5] == board[3] != " ": 
                declare_winner(turn)
                break
                
            elif board [1] == board[5] == board[9] != " ": 
                declare_winner(turn)
                break
        
    if count == 9:
        print("\nGame Over.\n")
        print("It's a Tie!!")

def declare_winner(turn):
    draw_board(board)
    if turn == "O":
        print("\nGame Over.\n")
        print(" **** " + player2 + " won *****")
    else:
        print("\nGame Over.\n")
        print(" **** " + player1 + " won *****")
    
    restart = input("\nDo you want to play again? (y/n):")
    if restart == "y" or restart == "Y":
            for element in board:
                board[board.index(element)] = " "
            game()
game()