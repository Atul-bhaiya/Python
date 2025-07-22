student_nav = []   #lists in python  # 🎓 Student Fee Tracker (Console App)

student_hafta = []
for i in range(3):
    student_name = input(f"Enter Student name :  {i+1}")
    student_fees = int(input(f"enter student fees:{i+1}"))
    student_nav.append(student_name)
    student_hafta.append(student_fees)

for i in range(3):
    print(f"\nStatus for {student_nav[i]}:")
    if student_hafta[i] >= 5000:
        print("✅ Paid in Full")
    else:
        pending = 5000 - student_hafta[i]
        print(f"⚠️ Pending Balance: ₹{pending}")

