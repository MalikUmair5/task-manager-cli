import json
import os

print("====== Task Manager ====== \n")
print("Select Any One Option")
print("1.  ➕ Add a Task")
print("2.  ❌ Remove a Task")
print("3.  ✅ Mark a Task as Done")
print("4.  📋 List All Tasks")
print("5.  🔴 Exit")



while True:
    try:
        selected_Option = int(input("Enter your Choice (1-5): "))
        if selected_Option in range(1, 6):
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
TASKS_FILE = "tasks.json"



def load_tasks():
    if os.path.exists(TASKS_FILE):  # File check karna
        with open(TASKS_FILE, "r") as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []  # Ensure list
            except json.JSONDecodeError:
                return []  # Agar file empty ya corrupt ho
    return []  # File exist nahi karti to empty list return karo

    
tasks = load_tasks() 

def add_tasks(title):
    task = {"Title": title, "Status": "pending"}
    tasks.append(task)
    save_tasks()


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)



if selected_Option == 1:
    task = input("Enter the task to add")
    add_tasks(task)







        

