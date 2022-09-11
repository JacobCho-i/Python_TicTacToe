
board = [[1,2,3],[4,5,6],[7,8,9]]
win = False
order = 0
player = ' '
WinCase = 0
def display_board():
    leng = len(board)
    for row in range(leng):
        sub = ""
        for col in range(leng):
            if col == leng-1:
                sub += str(board[row][col])
                sub += " "
            else:
                sub += str(board[row][col])
                sub += " l "
        print(sub)
        if row != leng - 1:
            print((3*leng) * "-")

def validMove(tile):
    if type(tile) != int:
        return False
    for row in range(3):
        for col in range(3):
            if board[row][col] == tile:
                return True
    return False
    


def checkWin():
    # 0 = ongoing
    # 1 = tie
    # 2 = x win
    # 3 = o win

    num_played = 0
    #horizontal row
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'x':
                return 2
            else:
                return 3
    #vertical row
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'x':
                return 2
            else:
                return 3
    #diagonal -> (0,0),(1,1),(2,2) or (0,2),(1,1),(2,0)
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][col] == 'x':
            return 2
        else:
            return 3
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][col] == 'x':
            return 2
        else:
            return 3
        
    #check for tie
    for row in range(3):
        for col in range(3):
            if type(board[col][row]) == str:
                num_played += 1

    if num_played == 9:
        return 1
    
    return 0

def translate(x):
    if x == 0:
        print("The game is still ongoing")
    if x == 1:
        print("The game is tied")
    if x == 2:
        print("x has won the game!")
    if x == 3:
        print("o has won the game!")
        
def check_player():
    if order % 2 == 0:
        return 'x'
    if order % 2 == 1:
        return 'o'
    
def mark_tile(tile):
    for row in range(3):
        for col in range(3):
            if board[row][col] == tile:
                board[row][col] = player

print()
while win == False:
        display_board()
        print()
        tile = int(input("Which tile are you going to play? "))
        if validMove(tile) == True:
            player = check_player()
            mark_tile(tile)
            order+=1
            print()
            print("***************************************************")
            print("            Successfully placed a tile!            ")
            print("***************************************************")
            print()
            if checkWin() == 1:
                display_board()
                print()
                print("***************************************************")
                print("                 The game is tied!                 ")
                print("***************************************************")
                print()
                win = True
            elif checkWin() == 2:
                #display_Winboard()
                display_board()
                print()
                print("***************************************************")
                print("                x has won the game!                ")
                print("***************************************************")
                print()
                win = True
            elif checkWin() == 3:
                #display_Winboard()
                display_board()
                print()
                print("***************************************************")
                print("                o has won the game!                ")
                print("***************************************************")
                print()
                win = True
        elif validMove(tile) == False:
            print()
            print("***************************************************")
            print("That tile either does not exist or is already used!")
            print()
            print("           Please select a valid tile!             ")
            print("***************************************************")
            print()
