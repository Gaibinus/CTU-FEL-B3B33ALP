#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 3

import sys

dataNum=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]
dataWord=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred','thousand']

def number(data):
    out=""
    if len(data)==6:
        out += dataWord[int(data[0])] + "hundred"
        if int(data[1])*10+int(data[2])<=20:
            out += dataWord[int(data[1]) * 10 + int(data[2])]
        else:
            out += dataWord[dataNum.index(int(data[1]) * 10)] + dataWord[int(data[2])]
        out += "thousand"

        out += dataWord[int(data[3])] + "hundred"
        if int(data[4])*10+int(data[5])<=20:
            out += dataWord[int(data[4]) * 10 + int(data[5])]
        else:
            out += dataWord[dataNum.index(int(data[4]) * 10)] + dataWord[int(data[5])]

    elif len(data)==5:
        if int(data[0])*10+int(data[1])<=20:
            out += dataWord[int(data[0])*10+int(data[1])]
        else:
            out += dataWord[dataNum.index(int(data[0])*10)] + dataWord[int(data[1])]
        out += "thousand"
        out += dataWord[int(data[2])] + "hundred"
        if int(data[3])*10+int(data[4])<=20:
            out += dataWord[int(data[3])*10+int(data[4])]
        else:
            out += dataWord[dataNum.index(int(data[3])*10)] + dataWord[int(data[4])]

    elif len(data)==4:
        out += dataWord[int(data[0])] + "thousand"
        if data[1]!='0' and data[2]!='0' and data[3]!='0':
            out += dataWord[int(data[1])] + "hundred"
        if int(data[2])*10+int(data[3])<=20:
            out += dataWord[int(data[2]) * 10 + int(data[3])]
        else:
            out += dataWord[dataNum.index(int(data[2])*10)] + dataWord[int(data[3])]

    elif len(data)==3:
        out += dataWord[int(data[0])] + "hundred"
        if int(data[1])*10+int(data[2])<=20:
            out += dataWord[int(data[1])*10 + int(data[2])]
        else:
            out += dataWord[dataNum.index(int(data[1])*10)] + dataWord[int(data[2])]

    elif len(data)>=2:
        if int(data[0])*10+int(data[1])<=20:
            out += dataWord[int(data[0])*10+int(data[1])]
        else:
            out += dataWord[dataNum.index(int(data[0])*10)] + dataWord[int(data[1])]

    elif len(data)==1:
        out+=dataWord[int(data[0])]

    else:
        error()

    return out

def word(data):
    value=[]
    posi=[]
    for i in range(37, 0, -1):
        for j in range(0, data.count(dataWord[i])):
            pos=data.find(dataWord[i])
            value.append(dataNum[i])
            posi.append(pos)
            data=data.replace(dataWord[i], '-'*int(len(dataWord[i])), 1)
    value=[x for _,x in sorted(zip(posi,value))]
    #print(value)
    #print(posi)

    out=0
    if value.count(1000)!=0:
        for i in range(0, value.index(1000), 1):
            if i!=value.index(1000)-1 and value[i]<=value[i+1]: error()
            out+=value[i]
        out*=1000

        for i in range(value.index(1000)+1, len(value), 1):
            if i != len(value) - 1 and value[i] <= value[i + 1]: error()
            out += value[i]

    else:
        for i in range(0, len(value), 1):
            if i != len(value) - 1 and value[i] <= value[i + 1]: error()
            out += value[i]

    if out==0: error()
    return out

def check(data):
    for i in range(37, 0, -1):
        #print(data)
        data=data.replace(dataWord[i], '0')
    sum=0
    for i in range(0, len(data), 1):
        if data[i]!='0': error()

def error():
    print("ERROR")
    sys.exit()

#main:
dataIn=str(input())

if dataIn[0].isdigit():
    print(number(dataIn))
else:
    check(dataIn)
    print(word(dataIn))