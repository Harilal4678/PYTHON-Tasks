class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f" name:{self.name}\n age:{self.age}")
class teacher(person):
    def __init__(self,subject):
        self.subject=subject

    def display(self,name,age):
        peron=person(name,age)
        peron.display()
        print(self.subject)

class student(person):
    def __init__(self,student_id):
        self.student_id=student_id

    def display(self,name,age):
        prsn=person(name,age)
        prsn.display()
        print(f"\nstudentid:{self.student_id}")

name=input("enter your name")
age=input("enter your age")
a=input("enter 1:teacher or 2:student")
if (a=="1" or a== "teacher"):
    sub=input("enter subject")
    teacher=teacher(sub)
    teacher.display(name,age)
else:
    stud_id=input("enter student id")
    student=student(stud_id)
    student.display(name,age)
