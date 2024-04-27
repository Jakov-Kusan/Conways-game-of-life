
def run(board,boardGeometry,generationLimit):
    for generation in range(generationLimit):
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
