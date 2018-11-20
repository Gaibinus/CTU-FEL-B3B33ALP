#Filip Geib filip@geib.sk
#CTU FEL KYR B3B33ALP 2018/19
#homework no. 5

import sys

#find position of king or queen
def possition(figure):
    r=-1
    c=-1
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if data[i][j]==figure:
                r=i
                c=j
    return str(r)+";"+str(c)

def countAttackers(tR,tC,side):
    count=0
    for r in range(0,8,1):
        for c in range(0,8,1):
            if r==tR and c==tC: pass
            elif movable(r,c,tR,tC,side)=="KILL": count+=1
    return count

#go thru whole array pointing to one figure
def scanArray(tR,tC,side):
    for r in range(0,8,1):
        for c in range(0,8,1):
            if r==tR and c==tC: pass
            elif movable(r,c,tR,tC,side)=="KILL": return str(r)+";"+str(c)
    return "NO"

#check if figurine can move to specific location
def movable(sR,sC,tR,tC,side):
    #test possibility; side=attacker side
    if side==-1:
        if data[tR][tC]<0: return "NO"
    else:
        if data[tR][tC]>0: return "NO"

    #king
    if data[sR][sC]==1*side:
        if abs(sR-tR)<=1 and abs(sC-tC)<=1:
            return "KILL"

    #pawn
    if data[sR][sC]==6*side:
        if side==-1:
            if data[tR][tC]==0:
                if tR-sR==-1 and tC-sC==0: return "KILL"
            else:
                if tR-sR==-1 and tC-sC==-1: return "KILL"
                elif tR-sR==-1 and tC-sC==1: return "KILL"
        else:
            if data[tR][tC]==0:
                if tR-sR==1 and tC-sC==0: return "KILL"
            else:
                if tR-sR==1 and tC-sC==1: return "KILL"
                elif tR-sR==-1 and tC-sC==1: return "KILL"

    #horse
    if data[sR][sC]==5*side:
        if abs(sR-tR)==2 and abs(sC-tC)==1: return "KILL"
        elif abs(sR-tR)==1 and abs(sC-tC)==2: return "KILL"

    #perpendicular queen or turret
    if data[sR][sC]==2*side or data[sR][sC]==3*side:
        if sR==tR:  #right
            for c in range(sC,tC+1,1):
                if c==tC: return "KILL"
                elif data[sR][c]!=0 and data[sR][c]!=-7 and c!=sC: break

        if sR==tR:  #left
            for c in range(sC,tC-1,-1):
                if c==tC: return "KILL"
                elif data[sR][c]!=0 and data[sR][c]!=-7 and c!=sC: break

        if sC==tC:  #down
            for r in range(sR,tR+1,1):
                if r==tR: return "KILL"
                elif data[r][sC]!=0 and data[r][sC]!=-7 and r!=sR: break

        if sC==tC:  #up
            for r in range(sR,tR-1,-1):
                if r==tR: return "KILL"
                elif data[r][sC]!=0 and data[r][sC]!=-7 and r!=sR: break

    #diagonal queen or archer
    if abs(sR-tR)==abs(sC-tC) and (data[sR][sC]==2*side or data[sR][sC]==4*side):
        c,r = sC,sR
        #right Up
        while r>0 and c<7:
            c+=1
            r-=1
            if c==tC and r==tR: return "KILL"
            elif data[r][c]!=0 and data[r][c]!=-7: break


        #right Down
        c,r = sC,sR
        while r<7 and c<7:
            c+=1
            r+=1
            if c==tC and r==tR: return "KILL"
            elif data[r][c]!=0 and data[r][c]!=-7: break

        #left Up
        c,r = sC,sR
        while r>0 and c>0:
            c-=1
            r-=1
            if c==tC and r==tR: return "KILL"
            elif data[r][c]!=0 and data[r][c]!=-7: break

        #left Down
        c,r = sC,sR
        while r<7 and c>0:
            c-=1
            r+=1
            if c==tC and r==tR: return "KILL"
            elif data[r][c]!=0 and data[r][c]!=-7: break

    return "NO"

def surrender(R,C):
    if R-1>=0: sR=R-1
    else: sR=R
    if C-1>=0: sC=C-1
    else: sC=C

    if R+1<=7: tR=R+1
    else: tR=R
    if C+1<=7: tC=C+1
    else: tC=C

    for c in range(sC,tC+1, 1):
        for r in range(sR,tR+1,1):
            if data[r][c]>=0:
                oldFigure=data[r][c]
                data[r][c]=-1
                val=scanArray(r,c,1)
                data[r][c]=oldFigure
                if val=="NO": return "YES"
    return val

def charge(aR,aC,kR,kC):
    #horse
    if data[aR][aC]==5:
        if scanArray(aR,aC,-1)!="NO": return "YES"

    #vertical
    elif abs(aC-kC)==0:
        if kR>aR:
            for r in range(aR,kR,1):
                if scanArray(r,aC,-1)!="NO": return "YES"
        else:
            for r in range(aR,kR,-1):
                if scanArray(r,aC,-1)!="NO": return "YES"

    #horizontal
    elif abs(aR-kR)==0:
        if kC>aC:
            for c in range(aC,kC,1):
                if scanArray(aR,c,-1)!="NO": return "YES"
        else:
            for r in range(aC,kC,-1):
                if scanArray(aR,c,-1)!="NO": return "YES"

    #diagonal
    else:
        r=aR
        c=aC
        while(aR!=kR or aC!=kC):
            if scanArray(r,c,-1)!="NO": return "YES"
            if kR-aR<0:
                if kC-aC<0:
                    r+=-1
                    c+=-1
                else:
                    r+=-1
                    c+=+1
            else:
                if kC-aC<0:
                    r+=+1
                    c+=-1
                else:
                    r+=+1
                    c+=+1

#main:
data=[]
f=open(sys.argv[1],'r')
for line in f:
    data.append(list(map(int, line.split())))

#king possition
pos=possition(-1)
pos=pos.split(';')
kR=int(pos[0])
kC=int(pos[1])

if countAttackers(kR,kC,1)>1:
    print("MAT")
    sys.exit()

attacker=scanArray(kR,kC,1)
if attacker!="NO":
    data[kR][kC]=-7
    if surrender(kR,kC)=="YES":
        print("SACH")
        sys.exit()
    attacker=attacker.split(";")
    if charge(int(attacker[0]),int(attacker[1]),kR,kC)=="YES":
        print("SACH")
        sys.exit()
    print("MAT")
    sys.exit()

#queen possition
pos=possition(-2)
pos=pos.split(';')
qR=int(pos[0])
qC=int(pos[1])
if scanArray(qR,qC,1)!="NO":
    print("GARDE")
    sys.exit()
else:
    print("NO")
    sys.exit()