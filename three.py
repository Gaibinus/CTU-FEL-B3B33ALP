#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 8

import sys
coun=0

def priArr(arr):
    for r in arr:
        print(r,sep='',end='')
    print()

def error():
    print("ERROR")
    sys.exit()

def out(a,b,c):
    global coun
    coun+=1
    print("t",coun,":=",a,b,c,sep='')

def numVar(char):
    if isinstance(char, int)==True: return True
    elif char.count('t')==1: return True
    else: return False

def bra(char):
    if ['(',')'].count(char)==1: return True
    else: return False

def symbHigh(char):
    if ['*','/','^'].count(char)==1: return True
    else: return False

def symbLow(char):
    if ['+','-'].count(char)==1: return True
    else: return False

def symb(char):
    if ['*','/','^','+','-'].count(char)==1: return True
    else: return False

def symbNull(char):
    if ['*','/','^','+'].count(char)==1: return True
    else: return False

def recursion(data):
    global coun
    #priArr(data)
    if len(data)==1: sys.exit()

    for i in range(0,len(data),1):
        if data[i]=='-':
            if numVar(data[i+1]) and (i==0 or numVar(data[i-1])==False):
                out(0,data[i],data[i+1])
                data[i]='t'+str(coun)
                del data[i+1]
                recursion(data)

        if data[i]=='(' and data[i+4]==')':
            out(data[i+1],data[i+2],data[i+3])
            data[i]='t'+str(coun)
            for j in range(0,4,1): del data[i+1]
            recursion(data)

        elif data[i]=='^' and numVar(data[i-1]) and numVar(data[i+1]):
            out(data[i-1],data[i],data[i+1])
            data[i-1]='t'+str(coun)
            for j in range(0,2,1): del data[i]
            recursion(data)

        elif (data[i]=='*' or data[i]=='/') and numVar(data[i-1])==True and numVar(data[i+1]):
            if i+2<len(data) and data[i+2]=='^' : pass
            else:
                out(data[i-1],data[i],data[i+1])
                data[i-1]='t'+str(coun)
                for j in range(0,2,1): del data[i]
                recursion(data)

        elif symbLow(data[i]) and numVar(data[i-1]) and numVar(data[i+1]):
            if i+2<len(data):
                if symbHigh(data[i+2])==False:
                    out(data[i-1],data[i],data[i+1])
                    data[i-1]='t'+str(coun)
                    for j in range(0,2,1): del data[i]
                    recursion(data)
            else:
                out(data[i-1],data[i],data[i+1])
                data[i-1]='t'+str(coun)
                for j in range(0,2,1): del data[i]
                recursion(data)

#main-------------------------------------------------------------------------------------------------------------------
inPut=input()
inPut=inPut.replace(' ','')

arr=[]
for i in range(0,len(inPut),1):
    if inPut[i].isdigit()==False:
        arr.append(inPut[i])
    else:
        if i!=0 and isinstance(arr[-1], int)==True:
            arr[-1]=arr[-1]*10+int(inPut[i])
        else:
            arr.append(int(inPut[i]))

#check for Errors in notation
if symbNull(arr[0]): error()
for i in range(0,len(arr),1):
    if numVar(arr[i]):
        if i!=0 and arr[i-1]==')' : error()
        if i+1<len(arr) and arr[i+1]=='(' : error()
    if symbNull(arr[i]):
        if i!=0 and arr[i-1]=='(' : error()
        if i+1<len(arr) and (arr[i+1]==')' or symbNull(arr[i+1])) : error()
    if symb(arr[i]):
        if i+1<len(arr) and (arr[i+1]==')' or symbNull(arr[i+1])) : error()
    if arr[i]=='^' and i+2<len(arr):
        if arr[i+2]=='(' : error()
    if arr[i]=='(' and i!=0 and arr[i-1]==')' : error()

recursion(arr)
