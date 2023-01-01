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
import csv
p=open("STUDENT.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    rss.append(r[0])
p.close()
g=open("FULL REPORT.txt","w")
g.close()
rw=1
print(rss)
while rw<len(rss):
    lst = []
    mno = []
    lqw = []
    #print("Enter The Student ID : ")
    id=rss[rw]
    p=open("COURSE.csv","r",newline="")
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

    g=open("FULL REPORT.txt","a")
    g.write("STUDENT ID : \n")
    g.write(ms[f]+"\n")
    g.write("NAME : \n")
    g.write(ms[f+1]+"\n")
    g.write("Class Roll Number : \n")
    g.write(ms[f+2]+"\n")
    g.write("Batch ID : \n")
    g.write(ms[f+3]+"\n")
    g.write("SUBJECTS : \n")
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
                g.write(mno[t]+"\n")
                g.write(ma + "\n")
                ov=int(ov)+int(ma)
                g.write("GRADE : "+mg + "\n")
                jy=jy+1
            fg=0
            u=u+1
        u=0
        t=t+1
    g.close()
    ov=str(ov)
    g=open("FULL REPORT.txt","a")
    g.write("Total : ")
    g.write(ov+"\n")
    ov=float(ov)
    ov=float(ov/(jy*100))
    ov=float(ov*100)
    g.write("Percentage : ")
    g.write(str(ov)+"%"+"\n")
    ov=float(ov)
    if float(ov) >= 90:
        g.write("Overall Grade : "+ "A"+"\n")
    if float(ov) >= 80 and float(ov) < 90:
        g.write("Overall Grade : " + "B" + "\n")
    if float(ov) >= 70 and float(ov) < 80:
        g.write("Overall Grade : " + "C" + "\n")
    if float(ov) >= 60 and float(ov) < 70:
        g.write("Overall Grade : " + "D" + "\n")
    if float(ov) >= 50 and float(ov) < 60:
        g.write("Overall Grade : " + "E" + "\n")
    if float(ov) >= 40 and float(ov) < 50:
        g.write("Overall Grade : " + "F" + "\n")
    if float(ov) < 40:
        g.write("Overall Grade : " + "G"  "\n")
    g.close()
    rw=rw+1
