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
rss=[]
per=[]
import csv
p=open("SUPPORT FILE.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    rss.append(r[0])
p.close()
g=open("FULL REPORT.txt","w")
g.close()
rw=1
raw=[]
#print(rss)
s=1
while s<len(rss):
    raw.append(rss[s])
    s=s+1
print(raw)
while rw<len(rss):
    lst = []
    mno = []
    lqw = []
    #print("Enter The Student ID : ")
    id=rss[rw]
    p=open("BASEFILE.csv","r",newline="")
    empdata=csv.reader(p)
    for r in empdata:
        lqw.append(r[0])
        mno.append(r[1])
        lst.append(r[2])
    p.close()
    ms=[]
    p=open("STUDENT.csv","r",newline="")
    empdata1=csv.reader(p)
    for r in empdata1:
        ms.append(r[0])
        ms.append(r[1])
        ms.append(r[2])
        ms.append(r[3])

    p.close()

    i=4
    f=0
    mnf=[]
    while i<len(ms):
        if ms[i]==id:
            f=i
        i=i+4


    t=1
    u=0
    ma=0
    mg=0
    fg=0
    jy=0
    ov = int(0)
    print(lst)
    while t<len(lst):
        m=modify(lst[t])
        m=modification(m)
        while u<len(m):
            if m[u]==ms[f]:
                ma=m[u+1]
                fg=1

                if int(m[u + 1]) >= 90:
                    mg = "A"

                if int(m[u + 1]) >= 80 and int(m[u + 1]) < 90:
                    mg = "B"

                if int(m[u + 1]) >= 70 and int(m[u + 1]) < 80:
                    mg = "C"

                if int(m[u + 1]) >= 60 and int(m[u + 1]) < 70:
                    mg = "D"

                if int(m[u + 1]) >= 50 and int(m[u + 1]) < 60:
                    mg = "E"

                if int(m[u + 1]) >= 40 and int(m[u + 1]) < 50:
                    mg = "F"

                if int(m[u + 1]) < 40:
                    mg = "G"

            if fg==1 :
                ov=int(ov)+int(ma)
                jy=jy+1
            fg=0
            u=u+1
        u=0
        t=t+1
    ov=str(ov)
    ov=float(ov)
    ov=float(ov/(jy*100))
    ov=float(ov*100)
    ov=float(ov)
    per.append(ov)
    rw=rw+1
print(per)
from matplotlib import pyplot as plt
student_performance=raw
student_values=per
plt.pie(student_values,labels=student_performance,startangle=90)
plt.show()