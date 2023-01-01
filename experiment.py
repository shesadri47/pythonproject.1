import csv
p=open("EXAMINATION_PERFORMANCE.csv","r",newline="")
empdata=csv.reader(p)
for r in empdata:
    print(r)
p.close()
