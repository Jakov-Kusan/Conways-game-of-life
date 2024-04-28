import time
def resetCellsToDraw():
    global boardGeometry
    global cellsToDraw

    for x in range(boardGeometry):
        for y in range(boardGeometry):
            cellsToDraw[x,y]=False

def start(bGeometry,wGeometry):
    global windowGeometry
    global boardGeometry
    global cellsToDraw
    # parameters cant be global
    windowGeometry=wGeometry
    boardGeometry=bGeometry
    cellsToDraw={}
    resetCellsToDraw()
    
def clear():
    global cellsToDraw
    global boardGeometry
    global windowGeometry

    # clearing
    for i in range(boardGeometry**2):
        print()

    # drawing the cells on screen
    # set to false if you want to remove the border
    border=True

    if border:
        print("__"+"_"*boardGeometry)
    for x in range(boardGeometry):
        if x!=0 and border:
            print("|")

        for y in range(boardGeometry):
            if y==0 and border:
                print("|",end="")
            if cellsToDraw[x,y]:
                print("#",end="")
            else:
                print(" ",end="")
    if border:
        print("|")
        print("--"+"-"*boardGeometry)

    time.sleep(1)
    # reseting the cells
    resetCellsToDraw()

def drawCell(x,y):
    global cellsToDraw
    cellsToDraw[x,y]=True
