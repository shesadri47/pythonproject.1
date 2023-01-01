print("Enter 1 To Update The  Name / 2 To Update The Class Roll Number / 3 To Update The Batch ID")
    ch=int(input())
    if ch==1 :
        import csv
        file=open('STUDENT.csv','r')
        Reader=csv.reader(file)
        L=[]
        id=input('Enter ID : ')
        Found=False
        for row in Reader:
            if row[0]==str(id):
                Found=True
                Salary=input('Enter The New Name : ')
                row[1]=Salary
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
    if ch==2 :
        import csv
        file=open('STUDENT.csv','r')
        Reader=csv.reader(file)
        L=[]
        id=input('Enter ID : ')
        Found=False
        for row in Reader:
            if row[0]==str(id):
                Found=True
                Salary=int(input('Enter The Class Roll Number : '))
                row[2]=Salary
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
    if ch==3 :
        import csv
        file=open('STUDENT.csv','r')
        Reader=csv.reader(file)
        L=[]
        id=input('Enter ID : ')
        Found=False
        for row in Reader:
            if row[0]==str(id):
                Found=True
                Salary=input('Enter The Batch ID : ')
                row[3]=Salary
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


