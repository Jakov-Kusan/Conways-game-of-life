
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
    for i in range(boardGeometry**3):
        print()

    # drawing the cells on screen
    for x in range(boardGeometry):
        for y in range(boardGeometry):
            if cellsToDraw[x,y]:
                print("#",end="")

            else:
                print(" ",end="")

    resetCellsToDraw()

def drawCell(x,y):
    global cellsToDraw
    cellsToDraw[x,y]=True
