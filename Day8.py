#Inheritense


class Employee:
    def __init__(self , name , salary ):
        self.name = name
        self.salary = salary
    def work(self):
        print("Doing general Employee task ")

class Manager(Employee):
    def manage_team(self):
        print("Managing the team ")


m1 = Manager("Atul", 50000)
m1.work()           # From Employee
m1.manage_team()    # From Manager
