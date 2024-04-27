# true if you want pygame as gui, false if you want terminal gui
pygame_gui=True

if pygame_gui:
    import pygameGui
    gui = pygameGui
else:
    import terminalGui
    gui = terminalGui
import time

def decideCellState(cellState,cellNeighbours):
    if cellNeighbours <2:
        return 0
    elif cellNeighbours >3:
        return 0
    elif cellNeighbours == 3:
        return 1
    else:
        return cellState


def getSurroundingCellNumber(board,x,y):
    surroundingCells=0
    try:
        if board[x+1,y]==1:
            surroundingCells=surroundingCells+1
    except:
        pass

    try:
        if board[x-1,y]==1:
            surroundingCells=surroundingCells+1
    except:
        pass
    
    try:
        if board[x,y+1]==1:
            surroundingCells=surroundingCells+1
    except:
        pass

    try:
        if board[x,y-1]==1:
            surroundingCells=surroundingCells+1
    except:
        pass

    try:
        if board[x+1,y+1]==1:
            surroundingCells=surroundingCells+1
    except:
        pass

    try:
        if board[x-1,y+1]==1:
            surroundingCells=surroundingCells+1
    except:
        time.sleep(0)

    try:
        if board[x+1,y-1]==1:
            surroundingCells=surroundingCells+1
    except:
        time.sleep(0)
    try:
        if board[x-1,y-1]==1:
            surroundingCells=surroundingCells+1
    except:
        time.sleep(0)
    
    return surroundingCells

def updateGui(board,boardGeometry):
    gui.clear()
    for x in range(boardGeometry):
            for y in range(boardGeometry):
                if board[x,y]==1:
                    gui.drawCell(x,y)

def run(board,boardGeometry,generationLimit):
    
    # main loop
    for generation in range(generationLimit):
        #drawing output
        updateGui(board,boardGeometry)
        time.sleep(1)
        print(generation)

        newBoard={}
        # updating cells
        for x in range(boardGeometry):
            for y in range(boardGeometry):
                newBoard[x,y]=decideCellState(board[x,y],getSurroundingCellNumber(board,x,y))
                
        board=newBoard




def main():
    board={}



    # boardGeometry*boardGeometry=cell number
    boardGeometry=100
    
    # stop on the 100th generation
    generationLimit=100

    for x in range(boardGeometry):
        for y in range(boardGeometry):
            # 0 if cell dead, 1 if alive
            board[x,y]=1
    
    # starting the gui
    windowGeometry=1000
    gui.start(boardGeometry,windowGeometry)

    run(board,boardGeometry,generationLimit)

if __name__ == "__main__":
    main()
