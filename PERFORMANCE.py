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

print("Enter The Course ID, To Check the Performance of Each Student Enrolled in that Course :")
cid=input()
lst=[]
import csv
p=open("COURSE.csv","r",newline="")
empdata=csv.reader(p)
t=1
for r in empdata:
    if r[0]==cid:
        lst.append(r[2])
        m = modify(lst[0])
        m = modification(m)
p.close()
u=len(m)
t=0
g=open("PERFOMANCE.txt","w")
g.write("Student ID"+"          "+"Name"+"                "+"Roll No."+"          "+"Marks"+"          "+"Grade"+"\n")
ax=1
mg=""
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0

while t<u:
    p=open("STUDENT.csv","r",newline="")
    empdata=csv.reader(p)
    for r in empdata:
        if r[0]==m[t]:
            g.write(r[0]+"             ")
            g.write(r[1]+"         ")
            g.write(r[2]+"                 ")
            g.write(m[ax]+"             ")
            if float(m[ax]) >= 90:
                mg = "A"
                a1=a1+1

            if float(m[ax]) >= 80 and float(m[ax]) < 90:
                mg = "B"
                a2 = a2 + 1

            if float(m[ax]) >= 70 and float(m[ax]) < 80:
                mg = "C"
                a3 = a3 + 1

            if float(m[ax]) >= 60 and float(m[ax]) < 70:
                mg = "D"
                a4 = a4 + 1

            if float(m[ax]) >= 50 and float(m[ax]) < 60:
                mg = "E"
                a5 = a5 + 1

            if float(m[ax]) >= 40 and float(m[ax]) < 50:
                mg = "F"
                a6 = a6 + 1

            if float(m[ax]) < 40:
                mg = "G"
                a7 = a7 + 1
            ax=ax+2
            g.write(str(mg) +"\n")

    p.close()
    t=t+2
g.close()