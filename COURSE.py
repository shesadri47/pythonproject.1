import csv
print("Enter The Number Of Student Data, You Want To Enter : ")
g=int(input())
p=open("COURSE.csv","w",newline='')
empdata=csv.writer(p)
empdata.writerow(["Course ID","Course Name","Marks obtained"])
for i in range(g):
    cd=input("Enter The Course ID :")
    cn=input("Enter The Course Name :")
    mo=input("Enter The Marks obtained : ")
    empinfo=[cd,cn,mo]
    empdata.writerow(empinfo)
    print("-------------------------------------------------------------------------------------")
p.close()