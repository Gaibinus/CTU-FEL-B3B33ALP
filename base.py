#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 2

base36 = "0123456789abcdefghijklmnopqrstuvwxyz"
import sys

def error():
    print("ERROR")
    sys.exit()

#check number base and format
def check(number, base):
    if number.count('.')>1: error()
    if number.count('-')>1: error()
    for i in range(0, len(number),1):
        if number[i]!='.' and number[i]!='-':
            if base36.count(number[i])==0: error()
            if base36.index(number[i])>base: error()
            if base36.index(number[i]) >= base: error()

#find starting power of 'to dec' chain
def startPow(number):
    if  number.count('.')>0:
        lenght=number.index('.')
    else:
        lenght = len(number)
    lenght-=1
    if number.count('-')>0: lenght-=1
    return lenght

#convert specific base to dec
def toDec(number, base):
    decimal=0
    power=startPow(number)
    for i in range(0, len(number), 1):
        if number[i]=='-' or number[i]=='.': pass
        else:
            decimal+=base36.index(number[i])*(base**power)
            power-=1
    if number[0] == '-': decimal *= -1
    return decimal

#convert dec to specific base
def toBase(decimal, base, prec):
    negative=False
    if decimal<0:
        negative=True
        decimal*=-1

    #at first integer part of the number
    intPart=[]
    integer=int(decimal)
    while integer!=0:
        intPart.insert(0, base36[integer%base])
        integer=integer//base
    if negative==True:
        intPart.insert(0, '-')
    intPart=''.join(str(A) for A in intPart)

    #than floating part of the number
    floatPart=[]
    floating=decimal-int(decimal)
    for i in range(0, prec+1, 1):
        floatPart.append(base36[int(floating*base)])
        floating=floating*base-int(floating*base)
        if i==prec:
            if base36.index(floatPart[i])>=base//2:
                floatPart[i-1]=base36[base36.index(floatPart[i-1])+1]
                floatPart.pop()
    floatPart=''.join(str(A) for A in floatPart)
    while len(floatPart)!=prec:
        floatPart=floatPart[:-1]

    if len(floatPart)!=0:
        return intPart+'.'+floatPart
    else:
        return  intPart

#find precision
def findPrec(number):
    if num1.count('.') == 1: return len(number)-number.index('.')-1
    else: return 0

#main:

base = int(input())
num1 = str(input())
num2 = str(input())

#numbers check
check(num1, base)
check(num2, base)

if findPrec(num1)>findPrec(num2): prec=findPrec(num1)
else: prec=findPrec(num2)

#numbers to decimal
num1=toDec(num1, base)
num2=toDec(num2, base)

#operation in dec
num=float(num1)-float(num2)

#ansver in specific base
print(toBase(num, base, prec))