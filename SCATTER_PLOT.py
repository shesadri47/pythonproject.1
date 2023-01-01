import csv
nam_lst=[]
id_lst=[]
srn_lst=[]
cou_lst=[]
mar_lst=[]
p=open("EXAMINATION_PERFORMANCE.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    nam_lst.append(r[0])
    id_lst.append(r[1])
    srn_lst.append(r[2])
    cou_lst.append(r[3])
    mar_lst.append(r[4])
p.close()
abn=[]
ab=[]
t=1
while t<len(id_lst):
    abn.append(id_lst[t])
    t=t+1
t=1
while t<len(mar_lst):
    ab.append(mar_lst[t])
    t=t+1


import matplotlib.pyplot as plt
x=ab
y=abn
plt.scatter(x,y)
plt.show()
