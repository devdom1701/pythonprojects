from student1 import Student
import csv

with open('sample_student_info.csv', newline='') as file:
    studentreader = csv.reader(file, delimiter=',', quotechar='|')
    studentreader.__next__()

    stliszt = []

    def searchreplace(item, replace, list_):
        for sublist in list_:
            for i in range(len(sublist)):
                if sublist[i] == item:
                    sublist[i] = replace

    def removeclass(list_, class_, cordx, cordy):
        if len(class_) > 0:
            print(class_)
        else:
            list_[cordx].pop(cordy)

    p = 0

    for i in studentreader:
        stliszt.append(i)

        searchreplace("Yes", True, stliszt)
        searchreplace("No", False, stliszt)

        s = Student(stliszt[p][0], stliszt[p][1], stliszt[p][2],
                    stliszt[p][3], stliszt[p][4], stliszt[p][5],
                    stliszt[p][6], stliszt[p][7], stliszt[p][8],
                    stliszt[p][9], stliszt[p][10], stliszt[p][11])
        print(s.first_name)
        print(s.last_name)
        print(s.gpa)
        removeclass(stliszt, s.class1, p, 4)
        removeclass(stliszt, s.class2, p, 5)
        removeclass(stliszt, s.class3, p, 6)
        removeclass(stliszt, s.class4, p, 7)
        print(s.age)
        print(s.student_id)
        print(s.email)
        print(s.is_enrolled)
        print(s.dateofbirth)

        p = p + 1
        print()