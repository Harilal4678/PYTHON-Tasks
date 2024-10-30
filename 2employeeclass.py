class employee:
    def __init__(self,id, name):
        self.id=id
        self.name=name

    def details(self):
         return(self.id,self.name)

    def calculate_pay(self):
        return("calculating payment...")

class houremployee(employee):
    def __init__(self, hourly_rate, hours_work):
        self.hourly_rate=hourly_rate
        self.hours_work=hours_work

    def calculate_pay(self):
        return self.hourly_rate*self.hours_work
    
class salaryemployee(employee):
    def __init__(self,salary):
        self.salary=salary

    def calculate_pay(self):
        return self.salary
    
emp=employee(7,"vini")


s=salaryemployee(1000)
print(emp.calculate_pay())
print(emp.details())
t=input("enter type of employee hour or salary \n")

if t=="hour":
    p=int(input("enter hours worked\n"))
    h=houremployee(1000,p)
    print(h.calculate_pay())
else:
    print(s.calculate_pay())




        