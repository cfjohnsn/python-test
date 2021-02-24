

def printboard():
    boardSize = 3
    x = 1
    while x <= boardSize:
        print (" ---" *boardSize + "\n" + "|   " *(boardSize+1))
        x = x+1
    print (' ---' * boardSize)


printboard()





