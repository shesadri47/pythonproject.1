def list_modifier(lst):
    i=0
    j=0
    arm=[]
    while i<len(lst):
        while j<len(lst[i]):
            arm.append(lst[i][j])
            j=j+1
        j=0
        i=i+1
    return arm

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
mok=[]
print("Enter The Department ID : ")
did=input()
import csv
p=open("DEPARTMENT.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    if did==r[0]:
        mok.append(r[2])
p.close()

m=modify(mok[0])
m=modification(m)
vbn=[]
t=0
while t<len(m):
    import csv
    p=open("STUDENT.csv","r",newline="")
    empdata=csv.reader(p)
    for r in empdata:
        if r[3]==m[t]:
            vbn.append(r[0])
    p.close()
    t=t+1
ln=0
while ln<len(vbn):
    lst=[]
    mno=[]
    lqw=[]
    #print("Enter The Student ID : ")
    id=vbn[ln]
    import csv
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

    t=1
    u=0
    ma=0
    mg=0
    fg=0
    jy=0
    msd=[]
    ov = int(0)
    while t<len(lst):
        m=modify(lst[t])
        m=modification(m)
        msd.append(m)
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
    ov=float(ov/jy)
    msd=list_modifier(msd)
    uv=0
    tyn=0
    fyn=0
    while uv<len(msd):
        if msd[uv]==vbn[ln]:
            tyn=float(tyn)+float(msd[uv+1])
            fyn=fyn+1
        uv=uv+1

    print(vbn[ln])
    gbn=(float(tyn/fyn))
    print("Average : "+str(gbn))


    ln=ln+1