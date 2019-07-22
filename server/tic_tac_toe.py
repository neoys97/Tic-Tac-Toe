n = 3
board = []
def createBoard(n):
    global board
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append("#")
        board.append(temp)

def printBoard():
    for line in board:
        for item in line:
            print (item, end= "\t")
        print()

def inputChoice(x,y,player):
    board[x][y] = player

def checkWin(player, board):
    for x in range (n):
        won = True
        for y in range (n):
            if board[x][y] != player:
                won = False
                break
        if won:
            return won
        won = True
        for y in range (n):
            if board[y][x] != player:
                won = False
                break
        if won:
            return won
    won = True
    for i in range (n):
        if board[i][i] != player:
            won = False
            break
    if won:
        return won
    won = True
    for i in range (n):
        if board[n-1-i][i] != player:
            won = False
            break
    return won

def checkEnd(board):
    n = len(board)
    for i in range (n):
        for j in range (n):
            if board[i][j]!="X" and board[i][j]!="O":
                return False
    return True

def start():
    createBoard(n)
    turn = 0
    player = ""
    win = ""
    while True:
        printBoard()
        if turn%2 == 0:
            player = "O"
        else:
            player = "X"
        turn += 1
        choice = 0
        while True:
            message = "Player " + player + " enter your choice: "
            choice = int(input(message))
            if (choice >= 0 and choice <= n*n-1) and (board[choice//n][choice%n] != "X" and board[choice//n][choice%n] != "O"):
                break
            else:
                print ("Invalid input, enter your choice again")
        inputChoice (choice//n, choice%n, player)  
        if(checkWin(player)):
            endGame = True
            win = player
            break
        if(checkEnd()):
            endGame = True
            break

    printBoard()
    if win:
        print ("Player", win, "wins")
    else:
        print("It's a draw")

def main():
    start()

if __name__ == "__main__":
    main()
