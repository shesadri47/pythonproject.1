def duplicator(tan):
    u=0
    while u<len(tan):
        if (u+1)<len(tan):
            if tan[u]==tan[u+1]:
                tan.pop(u+1)

        u=u+1
    return tan

def modification(mst):
    i = 0
    j = 0
    stv=""
    bv=[]
    while i < len(mst):
        while j < len(mst[i]):
            if m[i][j]!='-':
                stv=stv+m[i][j]
            j=j+1
        bv.append(stv)
        stv=""
        j=0
        i=i+1
    return bv
def modify(mst):
    mst=mst+":"
    u=0
    str=""
    hy=[]
    while u<len(mst):
        if mst[u]!=':'and mst!='-':
            str=str+mst[u]
        if mst[u]==':' or mst[u]=='-':
            hy.append(str)
            str=""
        u=u+1

    return hy
print("Enter The Batch ID : ")
bat=input()
mng=[]
import csv
p=open("STUDENT.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    if r[3]==bat:
        mng.append(r[0])
p.close()
mnf=[]
bng=[]
p=open("COURSE.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    bng.append(r[1])
    mnf.append(r[2])
p.close()
t=1
k=1
k2=0
k3=0
lmn=[]
while t<len(mnf):
    m=modify(mnf[t])
    m=modification(m)
    lmn.append(bng[t])
    lmn.append(m)
    t=t+1
vpn=[]
while k<len(lmn):
    while k2<len(lmn[k]):
        while k3<len(mng):
            if lmn[k][k2]==mng[k3]:
                vpn.append(lmn[k-1])
            k3=k3+1
        k3=0
        k2=k2+1
    k2=0
    k=k+2



print(duplicator(vpn))
