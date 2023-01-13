import numpy
import random


# 1. make the grid
grid = numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
#print(grid)

winKey = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],
[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]

def userPlay():
    choice = int(input('Enter a number between 1 - 9 for position :'))
    while choice < 1 and choice > 9:
        print('Enter a valid choice.')
        choice = int(input('Enter a number between 1 - 9 for position :'))
    if choice == 1:
        if grid[0][0] == 'X' or grid[0][0] == 'O':
            print('That position is taken.')
            userPlay()
        else:
            grid[0][0] = 'O'
    elif choice == 2:
        if grid[0][1] == 'O' or grid[0][1] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[0][1] = 'O'
    elif choice == 3:
        if grid[0][2] == 'O' or grid[0][2] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[0][2] = 'O'
    elif choice == 4:
        if grid[1][0] == 'O' or grid[1][0] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[1][0] = 'O'
    elif choice == 5:
        if grid[1][1] == 'O' or grid[1][1] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[1][1] = 'O'
    elif choice == 6:
        if grid[1][2] == 'O' or grid[1][2] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[1][2] = 'O'
    elif choice == 7:
        if grid[2][0] == 'O' or grid[2][0] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[2][0] = 'O'
    elif choice == 8:
        if grid[2][1] == 'O' or grid[2][1] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[2][1] = 'O'
    elif choice == 9:
        if grid[2][2] == 'O' or grid[2][2] == 'X':
            print('That position is taken.')
            userPlay()
        else:
            grid[2][2] = 'O'

def checkWhoWin():
    for i in winKey:
        l,m,n = i[0], i[1], i[2]
        if grid[l[0]][l[1]] == 'X' and grid[m[0]][m[1]] == 'X' and grid[n[0]][n[1]] == 'X':
            print('Computer wins.')
            exit()
        elif grid[l[0]][l[1]] == 'O' and grid[m[0]][m[1]] == 'O' and grid[n[0]][n[1]] == 'O':
            print('You win.')
            exit()

# if computer or user both are not winning then move
randomPlaces = []
def randomMove():
    for rp in winKey:
        l,m,n = rp[0], rp[1], rp[2]
        if grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == '_':
            randomPlaces.append(rp)   
    return random.choice(randomPlaces)

def computerWinning():
    for i in winKey:
        l,m,n = i[0], i[1], i[2]

        # if one place is empty
        if grid[l[0]][l[1]] == 'X' and grid[m[0]][m[1]] == 'X' and grid[n[0]][n[1]] == '_':
            grid[n[0]][n[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == 'X' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == 'X':
            grid[m[0]][m[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == 'X' and grid[n[0]][n[1]] == 'X':
            grid[l[0]][l[1]] = 'X'
            print(grid)
            break

        # if two places are empty
        elif grid[l[0]][l[1]] == 'X' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == '_':
            leftChoice = random.choice([grid[m[0]][m[1]],grid[n[0]][n[1]]])
            leftChoice = 'X'
            break
        elif grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == 'X' and grid[n[0]][n[1]] == '_':
            leftChoice = random.choice([grid[l[0]][l[1]],grid[n[0]][n[1]]])
            leftChoice = 'X'
            break
        elif grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == 'X':
            leftChoice = random.choice([grid[l[0]][l[1]],grid[m[0]][m[1]]])
            leftChoice = 'X'
            break
    # 7. game system checks if any one win exit
    checkWhoWin()

def computerChecksWinning():
    # computer checks if it is winning
    computerWinning()
    for i in winKey:
        l,m,n = i[0], i[1], i[2]

        # if one place is empty
        if grid[l[0]][l[1]] == 'O' and grid[m[0]][m[1]] == 'O' and grid[n[0]][n[1]] == '_':
            grid[n[0]][n[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == 'O' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == 'O':
            grid[m[0]][m[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == 'O' and grid[n[0]][n[1]] == 'O':
            grid[l[0]][l[1]] = 'X'
            print(grid)
            break
        
        # if one place is empty but different people
        elif grid[l[0]][l[1]] == 'X' and grid[m[0]][m[1]] == 'O' and grid[n[0]][n[1]] == '_':
            grid[n[0]][n[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == 'O' and grid[m[0]][m[1]] == 'X' and grid[n[0]][n[1]] == '_':
            grid[n[0]][n[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == 'O' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == 'X':
            grid[m[0]][m[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == 'X' and grid[m[0]][m[1]] == '_' and grid[n[0]][n[1]] == 'O':
            grid[m[0]][m[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == 'X' and grid[n[0]][n[1]] == 'O':
            grid[l[0]][l[1]] = 'X'
            print(grid)
            break
        elif grid[l[0]][l[1]] == '_' and grid[m[0]][m[1]] == 'O' and grid[n[0]][n[1]] == 'X':
            grid[l[0]][l[1]] = 'X'
            print(grid)
            break
    else:
        p = randomMove()
        if p == []:
            if grid[0][0] == '_':
                grid[0][0] = 'X'
            elif grid[0][1] == '_':
                grid[0][1] == 'X'
            elif grid[0][2] == '_':
                grid[0][2] == 'X' 
            elif grid[1][0] == '_':
                grid[1][0] == 'X' 
            elif grid[1][1] == '_':
                grid[1][1] == 'X' 
            elif grid[1][2] == '_':
                grid[1][2] == 'X' 
            elif grid[2][0] == '_':
                grid[2][0] == 'X' 
            elif grid[2][1] == '_':
                grid[2][1] == 'X' 
            elif grid[2][2] == '_':
                grid[2][2] == 'X'
        else:
            q,r,s = p[0], p[1], p[2]
            st = random.choice([q,r,s])
            grid[st[0]][st[1]] = 'X'
            print(grid)


# 2. who plays first - toss
tosses = [0,1]
toss = int(input('Enter 0 or 1 for toss :'))
while toss not in tosses:
    print('Please enter a valid choice.')
    toss = int(input('Enter 0 or 1 for toss :'))
if toss == random.choice(tosses):
    print('You win. You play first.')

    # 3. if user plays first then blank grid
    print(grid)
else:
    print('Computer wins. Computer plays first.')

    # 3. if computer plays first then random place
    places = random.choice(winKey)
    place = random.choice(places)
    x,y = place[0], place[1]
    grid[x][y] = 'X'
    print(grid)

# 8. Make a loop
while True:
    # 9. Check if all places are filled then no one wins
    goodToGo = True
    allPlaces = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    for i in allPlaces:
        if grid[i[0]][i[1]] == '_':
            goodToGo = False

    if goodToGo == True:
        print('No one wins.')
        exit()
    else:
        # 4. user plays
        userPlay()
        print(grid)

        # 7. game system checks if any one win exit
        checkWhoWin()

        # 5. computer checks if user is winning
        computerChecksWinning()

        # 7. game system checks if any one win exit
        checkWhoWin()




 