# Daily Notes Logger App (Console Project) Using File Handling

from datetime import datetime
note = input("Enter your Daily Note here ")
now =   datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
with open("notes.txt" , "a") as file:
    file.write(f"[{timestamp}] {note}\n")
    print("note saved completely  ")
    print("saved at ", timestamp)



