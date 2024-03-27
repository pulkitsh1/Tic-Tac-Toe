X=1
O=0

def setup_arena():
    return [[None,None,None],
            [None,None,None],
            [None,None,None]]

def pos_input(arena,row,column, turn):
    if turn == 'X':
        arena[row][column] = X
    else:
        arena[row][column] = O

def tic_tac_toe():
    arena = setup_arena()
    input_counter = 0
    # Here i have to take input from the user
    while input_counter <= 9:
        if input_counter % 2 == 0:
            pos_input(arena,'row','column',turn="O")
            input_counter += 1
            val=won_check()
            if val == True:
                return
        else:
            pos_input(arena,'row','column',turn="X")
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
    for i in range(0,3):
        if arena[i][j] == arena[i][j+1] and arena[i][j+1] == arena[i][j+2]:
            flag = True
            winner = arena[i][j]
        if flag == True:
            break
    if flag == False:
        for i in range(0,3):
            if arena[j][i] == arena[j+1][i] and arena[j+1][i] == arena[j+2][i]:
                flag = True
                winner = arena[i][j]
            if flag == True:
                break
    elif flag == False:
        i = 0
        if arena[j][i] == arena[j+1][i+1] and arena[j+1][i+1] == arena[j+2][i+2]:
            flag = True
            winner = arena[i][j]
    elif flag == False:
        i = 0
        j = 2
        if arena[i][j] == arena[i+1][j-1] and arena[i+1][j-1] == arena[i+2][i-2]:
            flag = True
            winner = arena[i][j]
    if flag == True:
        if winner == 1:
            print("2nd player is the winner!")
        else:
            print("1st player is the winner!")
        return True
    
    return False