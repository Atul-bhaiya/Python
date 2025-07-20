#Error Handling in Python

try:
    num1= float(input("Enter your Number 1 :"))
    num2= float(input("Enter your Number 2 :"))
    operator = input("Choose Operation (+, -, *, /): ")

    if operator == "+":
        print("Result =", num1+ num2)

    elif operator == "-":
        print("Result =", (num1-num2))

    elif operator == "*":
        print("Result =", (num1*num2))

    elif operator == "/":
        print("Result =", num1/num2)
    else:raise ValueError("you cannot perform calculation through these symbols or string ")
except ZeroDivisionError:
    print(" You cannot divide by 0.")
except ValueError as e:
    print("Error:", e)

finally:
    print("Calculation done ")






