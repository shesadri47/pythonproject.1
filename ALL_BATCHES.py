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
mnf=[]
print("Enter The Department ID : ")
did=input()
import csv
p=open("DEPARTMENT.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    if r[0]==did:
        mnf.append(r[2])
p.close()
m=modify(mnf[0])
m=modification(m)
t=0
while t<len(m):
    print(m[t])
    t=t+1