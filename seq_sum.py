#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 1

#main:

data = list(map(int, input().split()))
index = [0]*len(data)

#null positive and odd values
for i in range(0, len(data), 1):
    if data[i]>=0 or data[i]%2!=0:
        data[i]=0
#print(data)

#count in and de-creasing sequences
for i in range(0, len(data), 1):
    if data[i]!=0:
        f=i
        index[i]=1
        while data[f-1]<data[f]:
            f+=1
            if(data[f-1]!=0):
                index[i-1]+=1
            if f==len(data): #or i==len(data)-1:
                break
#print(index)

#find max
maximum=max(index)

#store maximas
maxPos=[]
for i in range(0, len(data), 1):
    if index[i]==maximum:
        maxPos.append(i)
#print(maxPos)

#count maxPos
for i in range(0, len(maxPos), 1):
    pos=maxPos[i]
    maxPos[i]=0
    for j in range(pos, pos+maximum, 1):
        maxPos[i]+=data[j]

#out for server evaluation
print(maximum)
print(max(maxPos))