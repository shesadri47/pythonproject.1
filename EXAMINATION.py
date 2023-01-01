import csv
print("Enter The Number Of Student Data, You Want To Enter : ")
g=int(input())
p=open("EXAMINATION_PERFORMANCE.csv","w",newline='')
empdata=csv.writer(p)
empdata.writerow(["STUDENT_NAME","STUDENT_ID","STUDENT_ROLL_NO.","COURSE_NAME","MARKS_OBTAINED"])
for i in range(g):
    stdnam=input("Enter The STUDENT NAME : ")
    stdid=input("Enter The STUDENT ID : ")
    stdcrn=int(input("Enter The STUDENT ROLL NO. : "))
    stdcou = input("Enter The COURSE NAME : ")
    stdmar = input("Enter The MARKS : ")
    empinfo=[stdnam,stdid,stdcrn,stdcou,stdmar]
    empdata.writerow(empinfo)
    print("-------------------------------------------------------------------------------------")
p.close()
