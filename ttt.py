import random

a = ['a', ' ', ' ', ' ']
b = ['b', ' ', ' ', ' ']
c = ['c', ' ', ' ', ' ']

matrix = [a, b, c]
x_labs = ['1', '2', '3']


def initialize():

    print("Welcome to Tic Tac Toe!\nWhere do you want to place your (X)?\n")
    print("   " + str(x_labs) + "\n")
    for line in matrix:
        print(line)
        print("\n")

def choice():
    while True:
        loc = input("Choose letter and number\n")
        if loc not in ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"):
            print("Sorry, but the chosen square could not be recognized.\nPlease select letter followed by number without a space")
        else:
            break
    mark(loc)

def mark(square):
    if check_space() == True:
        selection = square
        row_name = selection[0]
        column_name = selection[1]
        print(row_name)
        print(column_name)
        for line in matrix:
            if line[0] == row_name:
                if line[int(column_name)] == ' ':
                    line[int(column_name)] = 'X'
                else:
                    print("The cell is already occupied")
                    choice()
        for line in matrix:
            print(line)
            print("\n")
        if evaluate('X'):
            print("You win!")
        else:
            computer_play()
    else:
        print("The game is over")

def computer_play():
    if check_space() == True:
        could_write = False
        while could_write is False:
            column_selection = random.randint(1, 3)
            row_selection = random.choice(['a', 'b', 'c'])
            for line in matrix:
                if line[0] == row_selection:
                    if line[int(column_selection)] == ' ':
                        line[int(column_selection)] = 'O'
                        print("Put O")
                        could_write = True
                    else:
                        continue
        print("   " + str(x_labs) + "\n")
        for line in matrix:
            print(line)
            print("\n")
        if evaluate('O'):
            print("The computer wins")
        else:
            choice()
    else:
        print("The game is over")

def evaluate(x_or_o):
    win = False
    # Check row wise
    for line in matrix:
        count = 0
        for item in line:
            if item == x_or_o:
                count += 1
                if count == 3:
                    win = True
    # Check column wise
    for i in range(1, 4):
        count = 0
        for line in matrix:
            if line[i] == x_or_o:
                count += 1
                if count == 3:
                    win = True
    # Check diagonal wise (right)
    diag = 3
    pos = 1
    for line in matrix:
        if line[pos] != x_or_o:
            diag -= 1
        pos += 1
    if diag ==3:
        win = True
    # Check diagonal wise (left)
    diag = 3
    pos = 3
    for line in matrix:
        if line[pos] != x_or_o:
            diag -= 1
        pos -= 1
    if diag ==3:
        win = True
    return win

def check_space():
    space = False
    for line in matrix:
        for item in line:
            if item == ' ':
                space = True
    return space




initialize()
choice()
