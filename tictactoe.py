# Writeaprogramthatplaystic-tac-toe.Thetic-tac-toe
# game is played on a 3 3 grid as in the photo a the right.The © lepas2004/iStockphoto.
# game is played by two players, who take turns. The first player marks moves with a circle, the second with a cross. 
# The player who has formed a horizontal, vertical, or diag- onal sequence of three marks wins. 
# Your program should draw the game board, ask the user for the coordinates of the next mark, change the players after 
# every successful move, and pronounce the winner.

from math import*
from turtle import*


MAX_ROW = 3
MAX_COL = 3

def markOnTable(mark, table, player,t):
    row = int(mark[0]) - 1
    col = int(mark[2]) - 1
    if(player == 'x'):
        table[row][col] = player
        markOnTurtle(t, row, col, player)
    elif(player == 'o'):
        table[row][col] = player
        markOnTurtle(t, row, col, player)
    
def playGame(table, t):
    totalMove = 0
    boolVal = 1
    while(boolVal):
        player1Mark = input("Player1, enter the your next mark starting at row 1 and column 1 (row-column): ")
        
        markOnTable(player1Mark,table, 'x', t)
        totalMove += 1
        boolVal = checkForWinner(table,totalMove)
        if(boolVal == 0):
            return
        player2Mark = input("Player2, enter the your next mark starting at row 1 and column 1 (row-column): ")
        markOnTable(player2Mark,table, 'o', t)
        totalMove += 1
        boolVal = checkForWinner(table,totalMove)
 
def markOnTurtle(t, row, col, player):
    t.up() 
    t.goto(-160 + (170 * col) , 155 - (140 * row))
    t.down()
    if(player == 'o'):
        t.pensize(10)
        t.pencolor("red")
        t.circle(30)
    elif(player == 'x'):
        t.pensize(10)
        t.pencolor("black")
        drawX(t)

def drawX(t):
    t.seth(45)
    t.bk(50)
    t.seth(0)
    t.up()
    t.fd(35)
    t.seth(135)
    t.down()
    t.fd(50)
    
def drawGame(t):
    t.pensize(1)
    t.pencolor("black")
    t.up()
    t.home()
    t.goto(-90, 180)
    t.down()
    t.rt(90)
    t.fd(390)
    t.up()
    t.home()
    t.goto(90, 180)   
    t.down()
    t.rt(90)
    t.fd(390) 
    t.up()
    t.home()
    t.goto(200, 90)
    t.rt(180)
    t.down()
    t.fd(390)
    t.up()
    t.home()
    t.goto(200, -90)
    t.rt(180)
    t.down()
    t.fd(390)   

def checkForWinnerHelper(totalX, totalO):
    if (totalX == 3):
        print("Game over, Player1 won !!")
        return 1       
    elif (totalO == 3):
        print("Game over, Player2 won !!")
        return 1
    else:
        return 0

def checkForWinner(table, totalMove):
    totalX = 0
    totalO = 0
    if totalMove == 9:
        print("It's a tied.")
        return 0
    elif (totalMove > 4):
        for row in range(MAX_ROW):           
            for col in range(MAX_COL):
                if table[row][col] == 'x':
                    totalX += 1
                elif(table[row][col] == 'o'):
                    totalO += 1                    
            if(checkForWinnerHelper(totalX, totalO)):
                return 0
            else:
                totalX = 0
                totalO = 0
               
                
        for col in range(MAX_COL):           
            for row in range(MAX_ROW):
                if table[row][col] == 'x':
                    totalX += 1
                elif(table[row][col] == 'o'):
                    totalO += 1                   
            if(checkForWinnerHelper(totalX, totalO)):
                return 0
            else:
                totalX = 0
                totalO = 0
         
         
        for row in range(len(table)):            
            if table[row][row] == 'x':
                totalX += 1
            elif(table[row][row] == 'o'):
                totalO += 1
        if(checkForWinnerHelper(totalX, totalO)):
            return 0
        else:
            totalX = 0
            totalO = 0
         
                
        for row in range(2,-1, -1):
            if table[row][row] == 'x':
                totalX += 1
            elif(table[row][row] == 'o'):
                totalO += 1       
        if(checkForWinnerHelper(totalX, totalO)):
            return 0
        else:
            totalX = 0
            totalO = 0               
        return 1
      
    else:  
        return 1            
                
table = [['','',''],
         ['','',''],
         ['','','']]



t = Turtle()
t.hideturtle()
t.speed(100)
again = 'y'
while(again == 'y'):   
    drawGame(t)
    playGame(table,t)
    again =  input("Do you want to play again?(y/n)")
    t.clear()    
done() 
      
      
      
      
      
      
      
    