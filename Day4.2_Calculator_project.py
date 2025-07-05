#Making Calculator through Functions


def add(a,b):
    return a+b
def sub(a , b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

num1 = float(input("Enter Number 1 = "))
num2 = float(input("Enter Number 2 = "))
operator = input("Choose Operation (+, -, *, /): ")

if operator == "+":
    print("Result =", add(num1, num2))

elif operator == "-":
    print("Result =", sub(num1, num2))

elif operator == "*":
    print("Result =", multi(num1, num2))

elif operator == "/":
    print("Result =", div(num1, num2))

else:
    print("❌ Invalid operation")

recalculate = input("Want to recalculate another YES / NO ? ")

while True:

    num1 = float(input("Enter Number 1 = "))
    num2 = float(input("Enter Number 2 = "))
    operator = input("Choose Operation (+, -, *, /): ")

    if operator == "+":
        print("Result =", add(num1, num2))

    elif operator == "-":
        print("Result =", sub(num1, num2))

    elif operator == "*":
        print("Result =", multi(num1, num2))

    elif operator == "/":
        if num2 == 0:
            print("❌ Cannot divide by 0")
        else:
            print("Result =", div(num1, num2))
    else:
        print("❌ Invalid operation")

    # Ask if want to calculate again
    recalculate = input("Want to recalculate again? (yes/no): ").lower()
    if recalculate != "yes":
        print("Thank you for using the calculator Made by Atul bhaiya ")
        break









