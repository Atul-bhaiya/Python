
def calculate_percentage(m1,m2,m3):
    total = m1 + m2 + m3
    percentage = (total) / 300 * 100
    return percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 35:
        return "C"
    else:
        return "Fail ho gaye tum 😢"


mark1 = int(input("Enter mark 1 = "))
mark2 = int(input("Enter mark 2 = "))
mark3 = int(input("Enter mark 3 = "))

percentage = calculate_percentage(mark1 , mark2 , mark3 )
print("Total percentage  = ", percentage )
grade = get_grade(percentage)
print("Your Grade  ", grade)


