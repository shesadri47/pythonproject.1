import csv
print("Enter The Number Of Student Data, You Want To Enter : ")
g=int(input())
p=open("STUDENT.csv","w",newline='')
empdata=csv.writer(p)
empdata.writerow(["STUDENT ID","NAME","Class Roll Number","Batch ID"])
for i in range(g):
    stdid=input("Enter The Student ID :")
    stdname=input("Enter The Name :")
    stdcrn=int(input("Enter The Class Roll Number : "))
    stdbatid = input("Enter The Batch ID : ")
    empinfo=[stdid,stdname,stdcrn,stdbatid]
    empdata.writerow(empinfo)
    print("-------------------------------------------------------------------------------------")
p.close()
