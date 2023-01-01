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
mnf=[]
import csv
p=open("BATCH.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    if r[0]==bat :
        mnf.append(r[4])
p.close()
m=modify(mnf[0])
t=0
g=open("BATCH ID.txt","w")
g.write("STUDENT ID"+"        "+"Name"+"                 "+"Class Roll Number"+"\n")
g.close()
while t<len(m):
    import csv
    p=open("STUDENT.csv","r",newline="")
    empdata=csv.reader(p)
    for r in empdata:
        if r[0]==m[t]:
            g=open("BATCH ID.txt","a")
            g.write(m[t]+"        ")
            g.write(r[1]+"                 ")
            g.write(r[2]+"\n")
            g.close()
    p.close()
    t=t+1



