X=1
O=0

def setup_arena():
    return [[None,None,None],
            [None,None,None],
            [None,None,None]]

def pos_input(arena,row,column, turn):
    if turn == 'X':
        arena[row][column] = X
        return arena
    else:
        arena[row][column] = O
        return arena

def tic_tac_toe():
    arena = setup_arena()
    print(arena)
    input_counter = 0
    # Here i have to take input from the user
    while input_counter <= 9:
        if input_counter % 2 == 0:
            print("First Player")
            row = int(input("Row:"))
            col = int(input("Column:"))
            arena = pos_input(arena,row,col,turn="O")
            input_counter += 1
            val=won_check(arena)
            if val == True:
                return
        else:
            print("Second Player")
            row = int(input("Row:"))
            col = int(input("Column:"))
            arena = pos_input(arena,row,col,turn="X")
            input_counter += 1
            val=won_check(arena)
            if val == True:
                return
    if input_counter>9:
        print("Draw!")
    
def won_check(arena):
    flag = False
    j = 0
    winner = None
    print(arena)
    for i in range(0,3):
        if arena[i][j] == arena[i][j+1] and arena[i][j+1] == arena[i][j+2]:
            if arena[i][j]!= None:
                flag = True
                winner = arena[i][j]
                print(winner)
        if flag == True:
            break
    if flag == False:
        for i in range(0,3):
            if arena[j][i] == arena[j+1][i] and arena[j+1][i] == arena[j+2][i]:
                if arena[i][j]!= None: 
                    flag = True
                    winner = arena[i][j]
                    print("second")
                    print(winner)
            if flag == True:
                break
    if flag == False:
        i = 0
        if arena[j][i] == arena[j+1][i+1] and arena[j+1][i+1] == arena[j+2][i+2]:
            if arena[i][j]!= None:
                flag = True
                winner = arena[i][j]
    if flag == False:
        i = 0
        j = 2
        if arena[i][j] == arena[i+1][j-1] and arena[i+1][j-1] == arena[i+2][j-2]:
            if arena[i][j]!= None:
                flag = True
                winner = arena[i][j]
            
    if flag == True:
        if winner == 1:
            print("2nd player is the winner!")
        else:
            print("1st player is the winner!")
        return True
    
    return False

tic_tac_toe()