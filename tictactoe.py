


def printboard():
    boardSize = 3           #Variable decides how big the board is, could be made bigger or let user input.
    x = 1                   #starting point
    while x <= boardSize:   #Helps the program know when to stop
        print (" ---" *boardSize + "\n" + "|   " *(boardSize+1))    #Creates a row in the board.
        x = x+1                                                     #Helps the program know when to stop.
    print (' ---' * boardSize)   #Adds the last row


printboard()    #Calls the function





