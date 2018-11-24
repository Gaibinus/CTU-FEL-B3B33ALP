#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 6

import sys

def priArr(arr):
    print("-----------")
    for r in arr:
        print(' '.join([str(elem) for elem in r]))
    print("-----------")

def findRows(arr, row, col):
    rowIndex=[0]*col
    maxMatrix=0
    coords=[0]*2
    for r in range(0, row, 1):
        for c in range(0, col, 1):
             if arr[r][c]==0: rowIndex[c]=0
             else: rowIndex[c]+=1
        #print(rowIndex)

        stack=[-1]
        maxArea=0
        for i in range(0, col, 1):
            while stack[-1]!=-1 and rowIndex[stack[-1]]>=rowIndex[i]:
                last=stack.pop()
                maxArea=max(maxArea, rowIndex[last]*(i-stack[-1]-1))
                #print(r, ": ",rowIndex[last]," * ",(col-stack[-1]-1))
                #print("check ", maxArea, " / ", rowIndex[last]*(col-stack[-1]-1))

                #print(maxArea)
                if maxMatrix<maxArea:
                    maxMatrix=maxArea
                    coords[0]=r+1-rowIndex[last]
                    coords[1]=r
            stack.append(i)

        while stack[-1]!=-1:
            last=stack.pop()
            maxArea=max(maxArea, rowIndex[last]*(col-stack[-1]-1))
            #print(r, ": ",rowIndex[last]," * ",(col-stack[-1]-1))
            #print("max ", maxArea, " / ", rowIndex[last]*(col-stack[-1]-1))

            #print(maxArea)
            if maxMatrix<maxArea:
                maxMatrix=maxArea
                coords[0]=r+1-rowIndex[last]
                coords[1]=r


    return str(coords[0])+" "+str(coords[1])

#main
data=[]
f=open(sys.argv[1],'r')
for line in f:
    data.append(list(map(int, line.split())))

row=len(data)
col=len(data[0])

#negative to 1; positive and zero to 0
for r in range(0,row,1):
    for c in range(0,col,1):
        if data[r][c]>=0: data[r][c]=0
        else: data[r][c]=1

#priArr(data)
rows=findRows(data, row, col).split(" ")
data=list(zip(*data[::-1]))
#print("---")
#priArr(data)
columns=findRows(data, col, row).split(" ")
print(str(rows[0])+" "+str(columns[0]))
print(str(rows[1])+" "+str(columns[1]))