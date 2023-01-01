import csv
print("Enter The Number Of Student Data, You Want To Enter : ")
g=int(input())
p=open("BATCH.csv","w",newline='')
empdata=csv.writer(p)
empdata.writerow(["Batch ID","Batch Name","Department Name","List of Courses","List of Students"])
for i in range(g):
    bid=input("Enter The Batch ID :")
    bna=input("Enter The Batch Name :")
    dn=input("Enter The Department Name : ")
    co = input("Enter The Course : ")
    std = input("Enter The Student : ")
    empinfo=[bid,bna,dn,co,std]
    empdata.writerow(empinfo)
    print("-------------------------------------------------------------------------------------")
p.close()
