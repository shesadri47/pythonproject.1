print("                                                        Student Examination Portal                  ")
print("Enter 1 For The STUDENT Module")
print("Enter 2 For The COURSE Module")
print("Enter 3 For The BATCH Module")
print("Enter 4 For The DEPARTMENT Module")
print("Enter 5 For The EXAMINATION  Module")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
sq=int(input("Your Choice : "))
print("------------------------------------------------------------------------------------------------------------------------------------------------")
if sq==1:
    print("Enter 1 To Do Entry The Student Module")
    print("Enter 2 To Update The Student Module")
    print("Enter 3 To Remove a Student From The DataBase")
    print("Enter 4 To See The Report Card Of a Specific Student in a Text File")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    sq1 = int(input("Your Choice : "))
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    if sq1==1:
        import csv
        print("Enter The Number Of Student Data, You Want To Enter : ")
        g = int(input())
        p = open("STUDENT.csv", "w", newline='')
        empdata = csv.writer(p)
        empdata.writerow(["STUDENT ID", "NAME", "Class Roll Number", "Batch ID"])
        for i in range(g):
            stdid = input("Enter The Student ID :")
            stdname = input("Enter The Name :")
            stdcrn = int(input("Enter The Class Roll Number : "))
            stdbatid = input("Enter The Batch ID : ")
            empinfo = [stdid, stdname, stdcrn, stdbatid]
            empdata.writerow(empinfo)
            print("-------------------------------------------------------------------------------------")
        p.close()
    if sq1==2:
        print("Enter 1 To Update The  Name / 2 To Update The Class Roll Number / 3 To Update The Batch ID")
        ch = int(input())
        if ch == 1:
            import csv

            file = open('STUDENT.csv', 'r')
            Reader = csv.reader(file)
            L = []
            id = input('Enter ID : ')
            Found = False
            for row in Reader:
                if row[0] == str(id):
                    Found = True
                    Salary = input('Enter The New Name : ')
                    row[1] = Salary
                L.append(row)
            file.close()
            if Found == False:
                print('Employee Not Found')
            else:
                file = open('STUDENT.csv', 'w+', newline='')
                Writer = csv.writer(file)
                Writer.writerows(L)
                file.seek(0)
                Reader = csv.reader(file)
                for row in Reader:
                    print(row)
                file.close()
        if ch == 2:
            import csv

            file = open('STUDENT.csv', 'r')
            Reader = csv.reader(file)
            L = []
            id = input('Enter ID : ')
            Found = False
            for row in Reader:
                if row[0] == str(id):
                    Found = True
                    Salary = int(input('Enter The Class Roll Number : '))
                    row[2] = Salary
                L.append(row)
            file.close()
            if Found == False:
                print('Employee Not Found')
            else:
                file = open('STUDENT.csv', 'w+', newline='')
                Writer = csv.writer(file)
                Writer.writerows(L)
                file.seek(0)
                Reader = csv.reader(file)
                for row in Reader:
                    print(row)
                file.close()
        if ch == 3:
            import csv

            file = open('STUDENT.csv', 'r')
            Reader = csv.reader(file)
            L = []
            id = input('Enter ID : ')
            Found = False
            for row in Reader:
                if row[0] == str(id):
                    Found = True
                    Salary = input('Enter The Batch ID : ')
                    row[3] = Salary
                L.append(row)
            file.close()
            if Found == False:
                print('Employee Not Found')
            else:
                file = open('STUDENT.csv', 'w+', newline='')
                Writer = csv.writer(file)
                Writer.writerows(L)
                file.seek(0)
                Reader = csv.reader(file)
                for row in Reader:
                    print(row)
                file.close()
    if sq1 == 3:
        import csv
        file = open('STUDENT.csv', 'r')
        Reader = csv.reader(file)
        L = []
        id = input('Enter ID : ')
        Found = False
        for row in Reader:
            if row[0] == str(id):
                Found = True
            else:
                L.append(row)
        file.close()

        if Found == False:
            print('Employee Not Found')
        else:
            file = open('STUDENT.csv', 'w+', newline='')
            Writer = csv.writer(file)
            Writer.writerows(L)
            file.seek(0)
            Reader = csv.reader(file)
            for row in Reader:
                print(row)
            file.close()
    if sq1 == 4:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        lst = []
        mno = []
        lqw = []
        print("Enter The Student ID : ")
        id = input()
        import csv

        p = open("COURSE.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            lqw.append(r[0])
            mno.append(r[1])
            lst.append(r[2])
        p.close()
        ms = []
        p = open("STUDENT.csv", "r", newline="")
        empdata1 = csv.reader(p)
        for r in empdata1:
            ms.append(r[0])
            ms.append(r[1])
            ms.append(r[2])
            ms.append(r[3])

        p.close()

        i = 4
        f = 0
        mnf = []
        while i < len(ms):
            if ms[i] == id:
                f = i
            i = i + 4

        g = open("REPORT CARD.txt", "w")
        g.write("STUDENT ID : \n")
        g.write(ms[f] + "\n")
        g.write("NAME : \n")
        g.write(ms[f + 1] + "\n")
        g.write("Class Roll Number : \n")
        g.write(ms[f + 2] + "\n")
        g.write("Batch ID : \n")
        g.write(ms[f + 3] + "\n")
        g.write("SUBJECTS : \n")
        t = 1
        u = 0
        ma = 0
        mg = 0
        fg = 0
        jy = 0
        ov = int(0)
        while t < len(lst):
            m = modify(lst[t])
            m = modification(m)
            while u < len(m):
                if m[u] == ms[f]:
                    ma = m[u + 1]
                    fg = 1

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

                if fg == 1:
                    g.write(mno[t] + "\n")
                    g.write(ma + "\n")
                    ov = int(ov) + int(ma)
                    g.write("GRADE : " + mg + "\n")
                    jy = jy + 1
                fg = 0
                u = u + 1
            u = 0
            t = t + 1
        g.close()
        ov = str(ov)
        g = open("REPORT CARD.txt", "a")
        g.write("Total : ")
        g.write(ov + "\n")
        ov = float(ov)
        ov = float(ov / jy)
        if float(ov) >= 90:
            g.write("Overall Grade : " + "A" + "\n")
        if float(ov) >= 80 and float(ov) < 90:
            g.write("Overall Grade : " + "B" + "\n")
        if float(ov) >= 70 and float(ov) < 80:
            g.write("Overall Grade : " + "C" + "\n")
        if float(ov) >= 60 and float(ov) < 70:
            g.write("Overall Grade : " + "D" + "\n")
        if float(ov) >= 50 and float(ov) < 60:
            g.write("Overall Grade : " + "E" + "\n")
        if float(ov) >= 40 and float(ov) < 50:
            g.write("Overall Grade : " + "F" + "\n")
        if float(ov) < 40:
            g.write("Overall Grade : " + "G"  "\n")
        g.close()
        print("PLEASE OPEN REPORT CARD.txt FROM FILE SECTION TO SEE YOUR RESULT")
if sq==2:
    print("Enter 1 For Entry in Course Module")
    print("Enter 2 To View performance of all students in the course")
    print("Enter 3 To Show Histogram")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    sq1 = int(input("Your Choice : "))
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    if sq1==1:
        import csv

        print("Enter The Number Of Student Data, You Want To Enter : ")
        g = int(input())
        p = open("COURSE.csv", "w", newline='')
        empdata = csv.writer(p)
        empdata.writerow(["Course ID", "Course Name", "Marks obtained"])
        for i in range(g):
            cd = input("Enter The Course ID :")
            cn = input("Enter The Course Name :")
            mo = input("Enter The Marks obtained : ")
            empinfo = [cd, cn, mo]
            empdata.writerow(empinfo)
            print("-------------------------------------------------------------------------------------")
        p.close()

    if sq1 == 2:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        print("Enter The Course ID, To Check the Performance of Each Student Enrolled in that Course :")
        cid = input()
        lst = []
        import csv

        p = open("COURSE.csv", "r", newline="")
        empdata = csv.reader(p)
        t = 1
        for r in empdata:
            if r[0] == cid:
                lst.append(r[2])
                m = modify(lst[0])
                m = modification(m)
        p.close()
        u = len(m)
        t = 0
        g = open("PERFOMANCE.txt", "w")
        g.write(
            "Student ID" + "          " + "Name" + "                " + "Roll No." + "          " + "Marks" + "          " + "Grade" + "\n")
        ax = 1
        mg = ""
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        a5 = 0
        a6 = 0
        a7 = 0

        while t < u:
            p = open("STUDENT.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                if r[0] == m[t]:
                    g.write(r[0] + "             ")
                    g.write(r[1] + "         ")
                    g.write(r[2] + "                 ")
                    g.write(m[ax] + "             ")
                    if float(m[ax]) >= 90:
                        mg = "A"
                        a1 = a1 + 1

                    if float(m[ax]) >= 80 and float(m[ax]) < 90:
                        mg = "B"
                        a2 = a2 + 1

                    if float(m[ax]) >= 70 and float(m[ax]) < 80:
                        mg = "C"
                        a3 = a3 + 1

                    if float(m[ax]) >= 60 and float(m[ax]) < 70:
                        mg = "D"
                        a4 = a4 + 1

                    if float(m[ax]) >= 50 and float(m[ax]) < 60:
                        mg = "E"
                        a5 = a5 + 1

                    if float(m[ax]) >= 40 and float(m[ax]) < 50:
                        mg = "F"
                        a6 = a6 + 1

                    if float(m[ax]) < 40:
                        mg = "G"
                        a7 = a7 + 1
                    ax = ax + 2
                    g.write(str(mg) + "\n")

            p.close()
            t = t + 2
        g.close()
        print("PLEASE OPEN PERFORMANCE.txt FROM FILE SECTION")


    if sq1 == 3:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        print("Enter The Course ID, To Check the Performance of Each Student Enrolled in that Course :")
        cid = input()
        lst = []
        import csv

        p = open("COURSE.csv", "r", newline="")
        empdata = csv.reader(p)
        t = 1
        for r in empdata:
            if r[0] == cid:
                lst.append(r[2])
                m = modify(lst[0])
                m = modification(m)
        p.close()
        u = len(m)
        t = 0
        ax = 1
        mg = ""
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        a5 = 0
        a6 = 0
        a7 = 0

        while t < u:
            p = open("STUDENT.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                if r[0] == m[t]:
                    if float(m[ax]) >= 90:
                        mg = "A"
                        a1 = a1 + 1

                    if float(m[ax]) >= 80 and float(m[ax]) < 90:
                        mg = "B"
                        a2 = a2 + 1

                    if float(m[ax]) >= 70 and float(m[ax]) < 80:
                        mg = "C"
                        a3 = a3 + 1

                    if float(m[ax]) >= 60 and float(m[ax]) < 70:
                        mg = "D"
                        a4 = a4 + 1

                    if float(m[ax]) >= 50 and float(m[ax]) < 60:
                        mg = "E"
                        a5 = a5 + 1

                    if float(m[ax]) >= 40 and float(m[ax]) < 50:
                        mg = "F"
                        a6 = a6 + 1

                    if float(m[ax]) < 40:
                        mg = "G"
                        a7 = a7 + 1
                    ax = ax + 2
            p.close()
            t = t + 2
        mbs = []
        mbs.append(a1)
        mbs.append(a2)
        mbs.append(a3)
        mbs.append(a4)
        mbs.append(a5)
        mbs.append(a6)
        mbs.append(a7)
        i = 0
        j = 1
        f = 5
        x = []
        while i < len(mbs):
            while j <= mbs[i]:
                x.append(f)
                j = j + 1
            f = f + 10
            j = 1
            i = i + 1
        from matplotlib import pyplot as plt

        y = [1, 11, 21, 31, 41, 51, 61, 71]
        plt.hist(x, y, ec="yellow")
        plt.xlabel("GRADES")
        plt.ylabel("NUMBER OF STUDENTS")
        plt.title("NUMBER STUDENTS IN EACH GRADE : ")
        print("1-11 REPRESENTS A GRADE")
        print("11-21 REPRESENTS B GRADE")
        print("21-31 REPRESENTS C GRADE")
        print("31-41 REPRESENTS D GRADE")
        print("41-51 REPRESENTS E GRADE")
        print("51-61 REPRESENTS F GRADE")
        print("61-71 REPRESENTS G GRADE")

        plt.xticks(y)
        plt.show()
if sq==3:
    print("Enter 1 For Entry in Batch Module")
    print("Enter 2 To View list of all students in a batch")
    print("Enter 3 To View list of all courses taught in the batch")
    print("Enter 4 To View complete performance of all students in a batch")
    print("Enter 5 Pie Chart")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    sq1 = int(input("Your Choice : "))
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    if sq1==1:
        import csv
        print("Enter The Number Of Student Data, You Want To Enter : ")
        g = int(input())
        p = open("BATCH.csv", "w", newline='')
        empdata = csv.writer(p)
        empdata.writerow(["Batch ID", "Batch Name", "Department Name", "List of Courses", "List of Students"])
        for i in range(g):
            bid = input("Enter The Batch ID :")
            bna = input("Enter The Batch Name :")
            dn = input("Enter The Department Name : ")
            co = input("Enter The Course : ")
            std = input("Enter The Student : ")
            empinfo = [bid, bna, dn, co, std]
            empdata.writerow(empinfo)
            print("-------------------------------------------------------------------------------------")
        p.close()

    if sq1 == 2:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        print("Enter The Batch ID : ")
        bat = input()
        mnf = []
        import csv

        p = open("BATCH.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            if r[0] == bat:
                mnf.append(r[4])
        p.close()
        m = modify(mnf[0])
        t = 0
        g = open("BATCH ID.txt", "w")
        g.write("STUDENT ID" + "        " + "Name" + "                 " + "Class Roll Number" + "\n")
        g.close()
        while t < len(m):
            import csv

            p = open("STUDENT.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                if r[0] == m[t]:
                    g = open("BATCH ID.txt", "a")
                    g.write(m[t] + "        ")
                    g.write(r[1] + "                 ")
                    g.write(r[2] + "\n")
                    g.close()
            p.close()
            t = t + 1
        print("PLEASE OPEN BATCH ID.txt FROM FILE SECTION")
    if sq1 == 3:
        def duplicator(tan):
            u = 0
            while u < len(tan):
                if (u + 1) < len(tan):
                    if tan[u] == tan[u + 1]:
                        tan.pop(u + 1)

                u = u + 1
            return tan


        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        print("Enter The Batch ID : ")
        bat = input()
        mng = []
        import csv

        p = open("STUDENT.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            if r[3] == bat:
                mng.append(r[0])
        p.close()
        mnf = []
        bng = []
        p = open("COURSE.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            bng.append(r[1])
            mnf.append(r[2])
        p.close()
        t = 1
        k = 1
        k2 = 0
        k3 = 0
        lmn = []
        while t < len(mnf):
            m = modify(mnf[t])
            m = modification(m)
            lmn.append(bng[t])
            lmn.append(m)
            t = t + 1
        vpn = []
        while k < len(lmn):
            while k2 < len(lmn[k]):
                while k3 < len(mng):
                    if lmn[k][k2] == mng[k3]:
                        vpn.append(lmn[k - 1])
                    k3 = k3 + 1
                k3 = 0
                k2 = k2 + 1
            k2 = 0
            k = k + 2

        print(duplicator(vpn))
    if sq1 == 4:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        print("Enter The Course ID, To Check the Performance of Each Student Enrolled in that Course :")
        cid = input()
        lst = []
        import csv

        p = open("COURSE.csv", "r", newline="")
        empdata = csv.reader(p)
        t = 1
        for r in empdata:
            if r[0] == cid:
                lst.append(r[2])
                m = modify(lst[0])
                m = modification(m)
        p.close()
        u = len(m)
        t = 0
        g = open("PERFOMANCE.txt", "w")
        g.write(
            "Student ID" + "          " + "Name" + "                " + "Roll No." + "          " + "Marks" + "          " + "Grade" + "\n")
        ax = 1
        mg = ""
        a1 = 0
        a2 = 0
        a3 = 0
        a4 = 0
        a5 = 0
        a6 = 0
        a7 = 0

        while t < u:
            p = open("STUDENT.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                if r[0] == m[t]:
                    g.write(r[0] + "             ")
                    g.write(r[1] + "         ")
                    g.write(r[2] + "                 ")
                    g.write(m[ax] + "             ")
                    if float(m[ax]) >= 90:
                        mg = "A"
                        a1 = a1 + 1

                    if float(m[ax]) >= 80 and float(m[ax]) < 90:
                        mg = "B"
                        a2 = a2 + 1

                    if float(m[ax]) >= 70 and float(m[ax]) < 80:
                        mg = "C"
                        a3 = a3 + 1

                    if float(m[ax]) >= 60 and float(m[ax]) < 70:
                        mg = "D"
                        a4 = a4 + 1

                    if float(m[ax]) >= 50 and float(m[ax]) < 60:
                        mg = "E"
                        a5 = a5 + 1

                    if float(m[ax]) >= 40 and float(m[ax]) < 50:
                        mg = "F"
                        a6 = a6 + 1

                    if float(m[ax]) < 40:
                        mg = "G"
                        a7 = a7 + 1
                    ax = ax + 2
                    g.write(str(mg) + "\n")

            p.close()
            t = t + 2
        g.close()
        print("PLEASE OPEN PERFORMANCE.txt FROM FILE SECTION")
    if sq1 == 5:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        rss = []
        per = []
        import csv

        p = open("STUDENT.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            rss.append(r[0])
        p.close()
        g = open("FULL REPORT.txt", "w")
        g.close()
        rw = 1
        raw = []
        # print(rss)
        s = 1
        while s < len(rss):
            raw.append(rss[s])
            s = s + 1

        while rw < len(rss):
            lst = []
            mno = []
            lqw = []
            # print("Enter The Student ID : ")
            id = rss[rw]
            p = open("COURSE.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                lqw.append(r[0])
                mno.append(r[1])
                lst.append(r[2])
            p.close()
            ms = []
            p = open("STUDENT.csv", "r", newline="")
            empdata1 = csv.reader(p)
            for r in empdata1:
                ms.append(r[0])
                ms.append(r[1])
                ms.append(r[2])
                ms.append(r[3])

            p.close()

            i = 4
            f = 0
            mnf = []
            while i < len(ms):
                if ms[i] == id:
                    f = i
                i = i + 4

            t = 1
            u = 0
            ma = 0
            mg = 0
            fg = 0
            jy = 0
            ov = int(0)

            while t < len(lst):
                m = modify(lst[t])
                m = modification(m)
                while u < len(m):
                    if m[u] == ms[f]:
                        ma = m[u + 1]
                        fg = 1

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

                    if fg == 1:
                        ov = int(ov) + int(ma)
                        jy = jy + 1
                    fg = 0
                    u = u + 1
                u = 0
                t = t + 1
            ov = str(ov)
            ov = float(ov)
            ov = float(ov / (jy * 100))
            ov = float(ov * 100)
            ov = float(ov)
            per.append(ov)
            rw = rw + 1

        from matplotlib import pyplot as plt

        student_performance = raw
        student_values = per
        plt.pie(student_values, labels=student_performance, startangle=90)
        plt.show()
if sq==4:
    print("Enter 1 For Entry in Document Module")
    print("Enter 2 To View list of all students in a batch")
    print("Enter 3 To View average performance of all batches in the department")
    print("Enter 4 For Line Plot")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    sq1 = int(input("Your Choice : "))
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    if sq1 == 1:
        import csv
        print("Enter The Number Of Student Data, You Want To Enter : ")
        g = int(input())
        p = open("DEPARTMENT.csv", "w", newline='')
        empdata = csv.writer(p)
        empdata.writerow(["Department ID", "Department Name", "List of Batches"])
        for i in range(g):
            di = input("Enter The Department ID :")
            dn = input("Enter The Department Name :")
            ba = input("Enter The Batches : ")
            empinfo = [di, dn, ba]
            empdata.writerow(empinfo)
            print("-------------------------------------------------------------------------------------")
        p.close()
    if sq1==2:
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        mnf = []
        print("Enter The Department ID : ")
        did = input()
        import csv

        p = open("DEPARTMENT.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            if r[0] == did:
                mnf.append(r[2])
        p.close()
        m = modify(mnf[0])
        m = modification(m)
        t = 0
        while t < len(m):
            print(m[t])
            t = t + 1
    if sq1 == 3:
        def list_modifier(lst):
            i = 0
            j = 0
            arm = []
            while i < len(lst):
                while j < len(lst[i]):
                    arm.append(lst[i][j])
                    j = j + 1
                j = 0
                i = i + 1
            return arm


        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        mok = []
        print("Enter The Department ID : ")
        did = input()
        import csv

        p = open("DEPARTMENT.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            if did == r[0]:
                mok.append(r[2])
        p.close()

        m = modify(mok[0])
        m = modification(m)
        vbn = []
        t = 0
        while t < len(m):
            import csv

            p = open("STUDENT.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                if r[3] == m[t]:
                    vbn.append(r[0])
            p.close()
            t = t + 1
        ln = 0
        while ln < len(vbn):
            lst = []
            mno = []
            lqw = []
            # print("Enter The Student ID : ")
            id = vbn[ln]
            import csv

            p = open("COURSE.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                lqw.append(r[0])
                mno.append(r[1])
                lst.append(r[2])
            p.close()
            ms = []
            p = open("STUDENT.csv", "r", newline="")
            empdata1 = csv.reader(p)
            for r in empdata1:
                ms.append(r[0])
                ms.append(r[1])
                ms.append(r[2])
                ms.append(r[3])

            p.close()

            i = 4
            f = 0
            mnf = []
            while i < len(ms):
                if ms[i] == id:
                    f = i
                i = i + 4

            t = 1
            u = 0
            ma = 0
            mg = 0
            fg = 0
            jy = 0
            msd = []
            ov = int(0)
            while t < len(lst):
                m = modify(lst[t])
                m = modification(m)
                msd.append(m)
                while u < len(m):
                    if m[u] == ms[f]:
                        ma = m[u + 1]
                        fg = 1

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

                    if fg == 1:
                        ov = int(ov) + int(ma)
                        jy = jy + 1
                    fg = 0
                    u = u + 1
                u = 0
                t = t + 1
            ov = str(ov)
            ov = float(ov)
            ov = float(ov / jy)
            msd = list_modifier(msd)
            uv = 0
            tyn = 0
            fyn = 0
            while uv < len(msd):
                if msd[uv] == vbn[ln]:
                    tyn = float(tyn) + float(msd[uv + 1])
                    fyn = fyn + 1
                uv = uv + 1

            print(vbn[ln])
            gbn = (float(tyn / fyn))
            print("Average : " + str(gbn))

            ln = ln + 1
    if sq1 == 4:
        import matplotlib.pyplot as plt
        def modification(mst):
            i = 0
            j = 0
            stv = ""
            bv = []
            while i < len(mst):
                while j < len(mst[i]):
                    if m[i][j] != '-':
                        stv = stv + m[i][j]
                    j = j + 1
                bv.append(stv)
                stv = ""
                j = 0
                i = i + 1
            return bv


        def modify(mst):
            mst = mst + ":"
            u = 0
            str = ""
            hy = []
            while u < len(mst):
                if mst[u] != ':' and mst != '-':
                    str = str + mst[u]
                if mst[u] == ':' or mst[u] == '-':
                    hy.append(str)
                    str = ""
                u = u + 1

            return hy


        yui = []
        yut = []
        rss = []
        import csv

        p = open("STUDENT.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            rss.append(r[0])
        p.close()
        rw = 1
        while rw < len(rss):
            lst = []
            mno = []
            lqw = []
            # print("Enter The Student ID : ")
            id = rss[rw]
            p = open("COURSE.csv", "r", newline="")
            empdata = csv.reader(p)
            for r in empdata:
                lqw.append(r[0])
                mno.append(r[1])
                lst.append(r[2])
            p.close()
            ms = []
            p = open("STUDENT.csv", "r", newline="")
            empdata1 = csv.reader(p)
            for r in empdata1:
                ms.append(r[0])
                ms.append(r[1])
                ms.append(r[2])
                ms.append(r[3])

            p.close()

            i = 4
            f = 0
            mnf = []
            while i < len(ms):
                if ms[i] == id:
                    f = i
                i = i + 4
            yut.append(ms[f])
            t = 1
            u = 0
            ma = 0
            mg = 0
            fg = 0
            jy = 0
            ov = int(0)
            while t < len(lst):
                m = modify(lst[t])
                m = modification(m)
                while u < len(m):
                    if m[u] == ms[f]:
                        ma = m[u + 1]
                        fg = 1

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

                    if fg == 1:
                        ov = int(ov) + int(ma)
                        jy = jy + 1
                    fg = 0
                    u = u + 1
                u = 0
                t = t + 1
            ov = str(ov)
            ov = float(ov)
            ov = float(ov / (jy * 100))
            ov = float(ov * 100)
            yui.append(float(ov))
            ov = float(ov)
            rw = rw + 1
        year = yut
        unemply = yui
        plt.plot(year, unemply, marker="o")
        plt.xlabel("BATCH NAME")
        plt.ylabel("AVERAGE PERCENTAGE")
        plt.title("Average percentage of all students for each batch.")
        plt.show()
if sq==5:
    print("Enter 1 To Do Entry The Examination Module")
    print("Enter 2 To View Performance of all Students")
    print("Enter 3 To View in Scatter Plot")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    sq1 = int(input("Your Choice : "))
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    if sq1==1:
        import csv
        print("Enter The Number Of Student Data, You Want To Enter : ")
        g = int(input())
        p = open("EXAMINATION_PERFORMANCE.csv", "w", newline='')
        empdata = csv.writer(p)
        empdata.writerow(["STUDENT_NAME", "STUDENT_ID", "STUDENT_ROLL_NO.", "COURSE_NAME", "MARKS_OBTAINED"])
        for i in range(g):
            stdnam = input("Enter The STUDENT NAME : ")
            stdid = input("Enter The STUDENT ID : ")
            stdcrn = int(input("Enter The STUDENT ROLL NO. : "))
            stdcou = input("Enter The COURSE NAME : ")
            stdmar = input("Enter The MARKS : ")
            empinfo = [stdnam, stdid, stdcrn, stdcou, stdmar]
            empdata.writerow(empinfo)
            print("-------------------------------------------------------------------------------------")
        p.close()

    if sq1 == 2:
        import csv
        p = open("EXAMINATION_PERFORMANCE.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            print(r)
        p.close()
    if sq1==3:
        import csv

        nam_lst = []
        id_lst = []
        srn_lst = []
        cou_lst = []
        mar_lst = []
        p = open("EXAMINATION_PERFORMANCE.csv", "r", newline="")
        empdata = csv.reader(p)
        for r in empdata:
            nam_lst.append(r[0])
            id_lst.append(r[1])
            srn_lst.append(r[2])
            cou_lst.append(r[3])
            mar_lst.append(r[4])
        p.close()
        abn = []
        ab = []
        t = 1
        while t < len(id_lst):
            abn.append(id_lst[t])
            t = t + 1
        t = 1
        while t < len(mar_lst):
            ab.append(mar_lst[t])
            t = t + 1
        import matplotlib.pyplot as plt
        x = ab
        y = abn
        plt.scatter(x, y)
        plt.show()




