import csv
print("Enter The Number Of Student Data, You Want To Enter : ")
g=int(input())
p=open("DEPARTMENT.csv","w",newline='')
empdata=csv.writer(p)
empdata.writerow(["Department ID","Department Name","List of Batches"])
for i in range(g):
    di=input("Enter The Department ID :")
    dn=input("Enter The Department Name :")
    ba=input("Enter The Batches : ")
    empinfo=[di,dn,ba]
    empdata.writerow(empinfo)
    print("-------------------------------------------------------------------------------------")
p.close()
