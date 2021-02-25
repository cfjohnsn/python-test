gameover = False


gameboard = [[0, 0, 0],[0, 0, 0,], [0, 0, 0]]   #List of lists!

def show_game(player=0, x=0, y=0, just_display = False):                 #function!
    print ('   0  1  2')
    if not just_display:                                  #Makes sure the player put an input in
        gameboard [x][y] = player                           #Changes gameboard to add what the player put in.
    for count, row in enumerate(gameboard):                 #row is just each item in the list, in this example, each list.
        print (count, row)                                  #Printing the row is just printing the item on the list. 
    

def p1make_move():
    row = int(input('Player 1: Input your X coordinate: '))                 #Player 1 moves
    column = int(input('Player 1: Input your Y coordinate: '))
    show_game(player = 1, x = column, y = row, just_display= False)

def p2make_move():
    row = int(input('Player 2: Input your X coordinate: '))                 #Player 2 moves
    column = int(input('Player 2: Input your Y coordinate: '))
    show_game(player = 2, x = column, y = row, just_display= False)

show_game(just_display=True)

while gameover == False:
    p1make_move()
    p2make_move()










