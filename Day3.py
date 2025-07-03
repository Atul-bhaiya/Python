#✅ Login System Project

correct_username = "admin"
correct_password = "1234"

attempts = 1
while attempts <= 3 :
     username = input("Enter user name : ")
     password = int(input("Enter password "))
     if username == correct_username and password == correct_password :
         print("Login sucessful ")
         break
     else:
         print("Attempts left  = ", 3 - attempts )
     attempts +=1
     if attempts > 3:
         print("Account locked 🔒 Too many failed attempts.")

