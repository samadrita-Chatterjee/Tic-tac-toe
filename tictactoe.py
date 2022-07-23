
board=["-" for x in range(10)]
game_running = True
winner = None 
player1= "X"
def print_board():
    print(board[1] + " | " + board[2] +" | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] +" | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] +" | " + board[9])

def start_game():
    print_board()
    while game_running:
      player_input(player1)
      isgame_over()
      change_player()

    if winner== "X" or winner =="O":
      print(winner +  " has won the match")
    elif winner == None:
      print("It is tie")
    

def player_input(player):
    print(player +"'s turn ")
    pos=input("Choose a number between 1-9: ")
    free = False
    while not free:
      while pos not in ["1","2","3","4","5","6","7","8","9"]:
        pos= input("choose another number between 1 to 9 ")
      pos=int(pos)
      if board[pos] == "-":
        free = True
      else:
        print("This place is occupied! choose another one")
    
    board[pos]= player

    print_board()

def isgame_over():
   check_win()
   check_tie()

def check_win():
    global winner
    row_winner=check_row()
    column_winner=check_column()
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_row():
    global game_running
    row1= (board[1]== board[2]== board[3] != "-") 
    row2= (board[4]== board[5]== board[6] != "-")
    row3= (board[7]== board[8]== board[9] != "-") 
    if row1 or row2 or row3:
        game_running= False
    if row1:
        return  board[1]
    elif row2:
        return board[4]
    elif row3:
        return board[7]
    return   
        
def check_column():
    global game_running
    column1= (board[1]==board[4]==board[7] != "-") 
    column2= (board[2]==board[5]==board[8] != "-")
    column3= (board[3]==board[6]==board[9] != "-") 
    if column1 or column2 or column3:
       game_running=False
    if column1:
        return  board[1]
    elif column2:
        return board[2]
    elif column3:
        return board[3]
    return   
def check_diagonal():
    global game_running
    dia1= (board[1]==board[5]==board[9] != "-") 
    dia2= (board[3]==board[5]==board[7] != "-")
    
    if dia1 or dia2:
        game_running= False
    if dia1:
        return  board[1]
    elif dia2:
       return board[3]
    return



def check_tie():
    global game_running
    if "-" not in board:
      game_running = False
    
    return



def change_player():
    global player1
    if player1 == "X":
        player1= "O"
    elif player1 == "O":
        player1= "X" 
    return


start_game()
