#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 4

import sys

key="abcdefghijklmnopqrstuvwxyz"
sum=[0]*26
zero=[1]*26

def evaluate(original):
    check=0
    for i in range(0, len(sum), 1):
        check+=sum[i]*out[i]
    if check==0:
        for i in range(0, len(out), 1):
            original=original.replace(key[i], str(out[i]))
        print(original)
        sys.exit()

#main:
input=input()
input=input.lower()
original=str(input)

count=0
for i in range(0, 26, 1):
    if input.count(key[i])>0 : count+=1
if count>10:
    print("NONEXIST")
    sys.exit()

input=input.replace('-','+-')
input=input.split('=')

left=input[0].split('+')
right=input[1].split('+')

for i in range(0, len(left), 1):
    power = len(left[i]) - 1
    neg = 1
    for j in range(len(left[i])):
        if left[i][j]=='-':
            neg=-1
            zero[key.find(left[i][1])]=0
        else:
            if j==0: zero[key.find(left[i][0])]=0
            sum[key.find(left[i][j])]+=int((10**power)*neg)
        power-=1

for i in range(0, len(right), 1):
    power = len(right[i]) - 1
    neg = -1
    for j in range(len(right[i])):
        if right[i][j]=='-':
            neg=1
            zero[key.find(right[i][1])]=0
        else:
            if j == 0: zero[key.find(right[i][0])] = 0
            sum[key.find(right[i][j])]+=int((10**power)*neg)
        power-=1

while sum.count(0)!=0:
    index=sum.index(0)
    key=key.replace(key[index], '')
    del zero[index]
    del sum[index]

out=[0]*len(sum)

#continuously try everi number, break or skip every time when possible
for a in range(1-zero[0], 10, 1):
    out[0] = a
    if len(sum)>1 :
        for b in range(1 - zero[1], 10, 1):
            if b==a : pass
            else:
                out[1] = b
                if len(sum) > 2:
                    for c in range(1 - zero[2], 10, 1):
                        if c==a or c==b: pass
                        else:
                            out[2] = c
                            if len(sum) > 3:
                                for d in range(1 - zero[3], 10, 1):
                                    if d==a or d==b or d==c: pass
                                    else:
                                        out[3] = d
                                        if len(sum) > 4:
                                            for e in range(1 - zero[4], 10, 1):
                                                if e==a or e==b or e==c or e==d: pass
                                                else:
                                                    out[4] = e
                                                    if len(sum) > 5:
                                                        for f in range(1 - zero[5], 10, 1):
                                                            if f==a or f==b or f==c or f==d or f==e: pass
                                                            else:
                                                                out[5] = f
                                                                if len(sum) > 6:
                                                                    for g in range(1 - zero[6], 10, 1):
                                                                        if g==a or g==b or g==c or g==d or g==e or g==f:pass
                                                                        else:
                                                                            out[6] = g
                                                                            if len(sum) > 7:
                                                                                for h in range(1 - zero[7], 10, 1):
                                                                                    if h==a or h==b or h==c or h==d or h==e or h==f or h==g: pass
                                                                                    else:
                                                                                        out[7] = h
                                                                                        if len(sum) > 8:
                                                                                            for i in range(1 - zero[8], 10, 1):
                                                                                                if i==a or i==b or i==c or i==d or i==e or i==f or i==g or i==h: pass
                                                                                                else:
                                                                                                    out[8] = i
                                                                                                    if len(sum) > 9:
                                                                                                        for j in range(1 - zero[9], 10, 1):
                                                                                                            if j==a or j==b or j==c or j==d or j==e or j==f or j==g or j==h or j==i: pass
                                                                                                            else:
                                                                                                                out[9] = j
                                                                                                                if len(sum) > 10:
                                                                                                                    print("NONEXIST")
                                                                                                                    sys.exit()
                                                                                                                else:
                                                                                                                    evaluate(original)
                                                                                                    else:
                                                                                                        evaluate(original)
                                                                                        else:
                                                                                            evaluate(original)
                                                                            else:
                                                                                evaluate(original)
                                                                else:
                                                                    evaluate(original)
                                                    else:
                                                        evaluate(original)
                                        else:
                                            evaluate(original)
                            else:
                                evaluate(original)
                else:
                    evaluate(original)
    else:
        evaluate(original)

print("NONEXIST")
sys.exit()