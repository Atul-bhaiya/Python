# Day 1 for a revision for python in 7 days for testing today we will make ka project which will be based on the topics 🧾 🎯 Project Title: Personal Expense Tracker (Console App)
# 🔧 Topics Cover:
# print()
#
# input()
#
# Variables
#
# Type Conversion
#
# Basic Logic
#
# Bonus: if-else, round( )

print(" <<-- Welcome to personal expense tracker -->> ")
name = input("Enter your name : ")
budget = int(input("Enter your budget : "))
Food_expense  = int(input("Enter your food expense : "))
transport_expense  = int(input("Enter your transport expense : "))
shopping  = int(input("Enter your shopping  expense : "))

print(" <<-- Expense summary of your monthly salary -->> ")

total_expense = Food_expense + transport_expense + shopping
remaining = budget - total_expense

print(" <<-- Expense summary of  Mr.-->> " , name )
print("Total Expense ", total_expense)
print("Remaining = " , remaining)


# Advice based on budget
if total_expense > budget:
    print("⚠️ You are over budget! Be careful.")
elif total_expense == budget:
    print("💸 You used your full budget. Great planning!")
else:
    print("✅ Good job! You are under budget.")





