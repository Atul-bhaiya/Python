# ✅ Encapsulation Example

class Student:
    def __init__(self, marks, name):
        self.name = name
        self._marks = marks

    def get_marks(self):
        return self._marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
        else:
            print("Invalid Marks! Must be between 0 and 100.")

s1 = Student(85, "Atul")

print("Marks:", s1.get_marks())

s1.set_marks(95)
print("Updated Marks:", s1.get_marks())

s1.set_marks(-50)

