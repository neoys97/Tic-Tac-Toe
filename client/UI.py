from tkinter import *
import tic_tac_toe as ttt
import client

window = None
canvas = None
connection = None
avatar = "X"
boardInfo = [["#", "#", "#"],
             ["#", "#", "#"],
             ["#", "#", "#"]]
my_turn = False
endGame = False

def placeMark(mark, pos):
    col = pos % 3
    row = pos // 3
    tl = (col*100 + 20, row*100 + 20)
    br = (col*100 + 80, row*100 + 80)
    if mark == "O":
        canvas.create_oval(tl[0], tl[1], br[0], br[1], width=3)
    elif mark == "X":
        canvas.create_line(tl[0], tl[1], br[0], br[1], width=3)
        canvas.create_line(tl[0], br[1], br[0], tl[1], width=3)
    canvas.update()
        

def updateBoard():
    canvas.delete("all")
    n = len(boardInfo)
    for i in range (3):
        for j in range (3):
            tl = (0 + j*100, 0 + i*100)
            br = (100 + j*100, 100 + i*100)
            canvas.create_rectangle(tl[0],tl[1],br[0],br[1])
    for i in range (n):
        for j in range (n):
            placeMark(boardInfo[i][j], i*3+j)
    winCheck()

def selection(event):
    global boardInfo
    global endGame
    global my_turn
    
    if my_turn and not endGame:
        col = event.x // 100
        row = event.y // 100
        if boardInfo[row][col] == "#":
            boardInfo[row][col] = avatar
            client.send(connection)
            my_turn = False
            updateBoard()
            winCheck()
        else:
            print("Invalid input")

def winCheck():
    global endGame
    if ttt.checkWin("O", boardInfo):
        print ("O wins")
        endGame = True
    elif ttt.checkWin("X", boardInfo):
        print("X wins")
        endGame = True
    elif ttt.checkEnd(boardInfo):
        print("Game Over")
        endGame = True
        
def start(c):
    global window
    global canvas
    global connection
    connection = c
    window = Tk()
    canvas = Canvas(window, width=300, height=300)
    canvas.pack()
    for i in range (3):
        for j in range (3):
            tl = (0 + j*100, 0 + i*100)
            br = (100 + j*100, 100 + i*100)
            canvas.create_rectangle(tl[0],tl[1],br[0],br[1])
    canvas.bind("<Button-1>", selection)
    canvas.update()
    window.mainloop()
            
if __name__ == "__main__":
    start()
    
