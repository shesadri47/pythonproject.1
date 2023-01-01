import csv
file=open('STUDENT.csv','r')
Reader=csv.reader(file)
L=[]
id=input('Enter ID : ')
Found=False
for row in Reader:
    if row[0]==str(id):
        Found=True
    else:
        L.append(row)
file.close()

if Found==False:
    print('Employee Not Found')
else:
    file=open('STUDENT.csv','w+',newline='')
    Writer=csv.writer(file)
    Writer.writerows(L)
    file.seek(0)
    Reader=csv.reader(file)
    for row in Reader:
        print(row)
    file.close()
