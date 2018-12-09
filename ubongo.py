#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 7

import sys, copy

def priArr(arr):
    for r in arr:
        print(' '.join([str(elem) for elem in r]))

#rotate puzzle with 90*times degrees in negative direction
def rotateTimes(puzzle, times):
    for i in range(0, times, 1):
        puzzle=list(zip(*reversed(puzzle)))
    return puzzle

#remove specific puzzle from playfield
def undoPlacement(field, puzzle):
    for r in range(0,len(field),1):
        for c in range(0,len(field[0]),1):
            if field[r][c]==puzzle: field[r][c]=0
    return field

#check possibility and place puzzle at specific position
def placement(field, puzzle, posR, posC, no , rot):
    if rot%2==0:
        R=puzzles[0][no][0]
        if posR+R>puzzles[0][0][0]: return "ER-rdim"
        C=puzzles[0][no][1]
        if posC+C>puzzles[0][0][1]: return "ER-cdim"
    else:
        R=puzzles[0][no][1]
        if posR+R>puzzles[0][0][0]: return "ER-rdim"
        C=puzzles[0][no][0]
        if posC+C>puzzles[0][0][1]: return "ER-cdim"

    #check if is free in shape of the puzzle
    for r in range(0,R,1):
        for c in range(0,C,1):
            if puzzle[r][c]!=0:
                if field[posR+r][posC+c]!=0: return "ER-puzfit"
    #put puzzle in specific area
    for r in range(0,R,1):
        for c in range(0,C,1):
            if puzzle[r][c]!=0: field[posR+r][posC+c]=puzzle[r][c]
    return "OK"

def recursion(puzzles, index, matrix, R, C, last):
    if len(index)==0:
        priArr(matrix)
        sys.exit()

    for r in range(0,R,1):
        for c in range(0,C,1):
            for puz in range(1,len(index)+1,1):
                test=index.pop(0)
                for rot in range(0,4,1):
                    if placement(matrix,rotateTimes(puzzles[test],rot),r,c,test,rot)=="OK":
                        recursion(puzzles, index, matrix, R, C, test)
                index.append(test)
    undoPlacement(matrix,last)

#main-------------------------------------------------------------------------------------------------------------------
matrix=[] #playfield matrix
puzzles=[] #array of puzzles
puzzSum=0

data=[]
file=open(sys.argv[1],'r')

#process input
for i, line in enumerate(file):
    if i == 0:
        data=line.split()
        puzzles.append([])
        puzzles[0].append([])
        puzzles[0][0].append(int(data[1]))
        puzzles[0][0].append(int(data[0]))

    elif i>=1 and i<=int(data[1]):
        matrix.append(list(map(int, line.split())))

    elif i>int(data[1]):
        puzzSum+=1
        data=(list(map(int, line.split())))
        xMax=0
        yMax=0
        for j in range(0,len(data),1):
            if j%2==0 and data[j]>xMax: xMax=data[j]
            elif data[j]>yMax: yMax=data[j]
        xMax,yMax=xMax+1,yMax+1
        #set puzzle size into memory
        puzzles[0].append([])
        puzzles[0][puzzSum].append(yMax)
        puzzles[0][puzzSum].append(xMax)
        #create zero matrix with specific size of puzzle block
        puzzles.append([[0 for x in range(xMax)] for y in range(yMax)])
        #fill created matrix with puzzle numbers
        for j in range(0,len(data),1):
            if j%2==1:
                puzzles[puzzSum][yMax-1-data[j]][data[j-1]]=puzzSum
file.close()

index=[]
for i in range(1,puzzSum+1,1):
    index.append(i)

recursion(puzzles, index, matrix, len(matrix), len(matrix[0]), 1)