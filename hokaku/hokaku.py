from pprint import pprint
# n = int(input())

# 6 x 5 matrix
grid = [[0 for i in range(5)] for i in range(6)]

pprint(grid)

# KEY
#
# 0 => empty cell
# 1 => playerOneOwned
# 2 => playerOneShrine **
# 3 => playerTwoOwned
# 4 => playerTwoShrine **
# 5 => ownedBoth

# Game will end when a player cannot place down a shrine.
# Tiles can be controlled by shrines of different colours

# for example if a cell is controlled by both colours,
# then no one can place another shrine there.

playerOneTurn = True

def fix(x, y):
    # x - 1
    # max(0, x - 1)
    # min(x + 1, m)
    return (min(max(0, x), 5), min(max(0, y), 4))

def good(x, y, playerOneTurn):
    if x < 0 or x > 5 or y < 0 or y > 4:
        return False 
    
    if playerOneTurn:
        return grid[x][y] in [0, 1]
    else:
        return grid[x][y] in [0, 3]

def fill(x, y, playerOneTurn):
    if playerOneTurn:
        if grid[x][y] == 0:
            grid[x][y] = 1
        if grid[x][y] == 3:
            grid[x][y] = 5
    else:
        if grid[x][y] == 0:
            grid[x][y] = 3
        if grid[x][y] == 1:
            grid[x][y] = 5
        
while True:

    # assume valid x, y
    b = input()
    x, y = map(int, b.split())

    if not good(x, y, playerOneTurn):
        print("Cannot place there")
        continue

    if playerOneTurn:
        grid[x][y] = 2
    else:
        grid[x][y] = 4

    # whenever we place down a shrine, fill neighbours
    for i in range(-1, 2):
        if i == 0: continue
        fill(*fix(x+i, y), playerOneTurn)
        fill(*fix(x, y+i), playerOneTurn)
        
    pprint(grid)
    playerOneTurn = not playerOneTurn


