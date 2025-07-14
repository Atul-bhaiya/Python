#Started Object oriented concepts OOPs
#class and object

class Student:
    def __init__( self , name , marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"MR {self.name} got Marks {self.marks}")

student1 = Student("Atul", 99 )
student2 = Student("AAyush ", 49 )

student1.display_details()
student2.display_details()
