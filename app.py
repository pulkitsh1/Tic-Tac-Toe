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
            val=won_check()
            if val == True:
                return
    if input_counter>9:
        print("Draw!")
    
def won_check():
    pass
