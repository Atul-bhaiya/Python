#💻 Mini Project for Day 2 – Marks Grader App 🎓
#🔧 Topics Covered:
#input(), int()
#if-elif-else
#Logical thinking
#and/or usage

print("<<--------------Welcome to Marks Grader App --------->>")
Student_name = input("Enter student Name :  ")
Marks = int(input("Enter your marks :"))
print(f"your result : {Marks} of {Student_name}")


if Marks >100 or Marks<0 :
    print("Invaild Marks Entered ")

elif Marks>= 90 :
    print("Grade A+")
elif Marks >= 75 :
    print("Grade A")
elif Marks>= 60 :
    print("Grade B")
elif Marks>= 50 :
    print("Grade C")

elif Marks>= 35:
    print("Grade D ( Pass ) ")
else :
    print("Grade F ( Fail ) ")
