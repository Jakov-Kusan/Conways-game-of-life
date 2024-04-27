# true if you want pygame as gui, false if you want terminal gui
pygame_gui=True

if pygame_gui:
    import pygameGui
else:
    import terminalGui

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
    if board[x+1,y]==1:
        surroundingCells=surroundingCells+1

    if board[x-1,y]==1:
       surroundingCells=surroundingCells+1
    
    if board[x,y+1]==1:
       surroundingCells=surroundingCells+1
    
    if board[x,y-1]==1:
       surroundingCells=surroundingCells+1
    
    if board[x+1,y+1]==1:
        surroundingCells=surroundingCells+1

    if board[x-1,y+1]==1:
       surroundingCells=surroundingCells+1

    if board[x+1,y-1]==1:
        surroundingCells=surroundingCells+1

    if board[x-1,y-1]==1:
       surroundingCells=surroundingCells+1

    
    return surroundingCells
def run(board,boardGeometry,generationLimit):
    
    # main loop
    for generation in range(generationLimit):
        newBoard={}
        
        # updating cells
        for x in range(boardGeometry):
            for y in range(boardGeometry):
                newBoard[x,y]=decideCellState(board[x,y],getSurroundingCellNumber(board,x,y))
                
        board=NewBoard




def main():
    board={}



    # boardGeometry*boardGeometry=cell number
    boardGeometry=10
    
    # stop on the 100th generation
    generationLimit=100


    for x in range(boardGeometry):
        for y in range(boardGeometry):
            # 0 if cell dead, 1 if alive
            board[x,y]=0




    print(board)
if __name__ == "__main__":
    main()
