#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    pLoc = -1
    #find the x and y for 'p'
    for i in range(0, m):
        if (grid[i].find('p') != -1):
            pyLoc = i
            pxLoc = grid[i].find('p')
            #print(pyLoc)
            #print(pxLoc)
    for i in range(0, m):
        if (grid[i].find('m') != -1):
            myLoc = i
            mxLoc = grid[i].find('m')
            #print(myLoc)
            #print(mxLoc)
    yMov = myLoc - pyLoc
    xMov = mxLoc - pxLoc
    #print(yMov)
    #print(xMov)
    if (yMov > 0):
        for j in range(0, abs(yMov)):
            print('UP')
    else:
        for j in range(0, abs(yMov)):
            print('DOWN')

    if (xMov > 0):
        for j in range(0, abs(xMov)):
            print('LEFT')
    else:
        for j in range(0, abs(xMov)):
            print('RIGHT')

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
