#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 10

import sys

debug = False

#insert items to buffer, erasing front because of ceeping len(buf)<=32
def addToBuf(str, add):
    correct=len(str)+len(add)-32
    if correct>0: str=str[correct:]+add
    else: str+=add
    return str

#output modes: debug / required
def printSpec(offset, length):
    if debug == True: print('(',offset,',',length,')',sep='',end='')
    else: print(chr(0x80 | (offset << 2) | ((length-2)&0x3)),sep='',end='')

#main-------------------------------------------------------------------------------------------------------------------
#decode
if len(sys.argv)==2 and sys.argv[1]=='-d':
    for line in sys.stdin:
        buf=""
        for i in range(0,len(line),1):
            if ord(line[i])<128:
                print(line[i],sep='',end='')
                buf=addToBuf(buf,line[i])
            else:
                leng=2+(ord(line[i])&3)
                offs=((ord(line[i])>>2) & 0x1f)
                print(buf[offs:offs+leng],sep='',end='')
                buf=addToBuf(buf,buf[offs:offs+leng])

#code
else:
    for line in sys.stdin:
        i=0
        buf=""
        while i < len(line):
            if buf.find(line[i:i+5])!=-1:
                printSpec(buf.find(line[i:i+5]),5)
                buf=addToBuf(buf,line[i:i+5])
                i+=5
            elif buf.find(line[i:i+4])!=-1:
                printSpec(buf.find(line[i:i+4]),4)
                buf=addToBuf(buf,line[i:i+4])
                i+=4
            elif buf.find(line[i:i+3])!=-1:
                printSpec(buf.find(line[i:i+3]),3)
                buf=addToBuf(buf,line[i:i+3])
                i+=3
            elif buf.find(line[i:i+2])!=-1:
                printSpec(buf.find(line[i:i+2]),2)
                buf=addToBuf(buf,line[i:i+2])
                i+=2
            else:
                print(line[i],sep='',end='')
                buf=addToBuf(buf,line[i])
                i+=1