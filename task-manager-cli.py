import json
import os







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
    if save_tasks():
        return True
    else:
        return False
    
def remove_task(id):
 #   print("Task Removed Successfully")
    print(tasks[id -1])
    tasks.pop(id - 1)
    save_tasks()
    

def show_all_tasks():
    i = 1
    for task in tasks:
        print(f"{i}) {task["Title"]} [{task["Status"]}]")
        i += 1



def save_tasks():
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
            return True
    except Exception:
        print(f"Error Saving Tasks {Exception}")
        return False







while True:
    try:
        print("====== Task Manager ====== \n")
        print("Select Any One Option")
        print("1.  ➕ Add a Task")
        print("2.  ❌ Remove a Task")
        print("3.  ✅ Mark a Task as Done")
        print("4.  📋 List All Tasks")
        print("5.  🔴 Exit")

        selected_Option = int(input("Enter your Choice (1-5):"))

        if selected_Option in range(1, 6):

            if selected_Option == 1:
                print("\n")
                task = input("Enter the task to add: ")
                print("\n")
                if add_tasks(task):
                    print("✔️ Task Added Successfully \n")
                else:
                    print("Some Error Accoured \n")

            elif selected_Option == 2:
                print("\n")
                show_all_tasks()
                print("\n")
                id = int(input("Enter Task Number To Delete: "))
                remove_task(id)
                print("\n")
            elif selected_Option == 5:
                break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
            print("❌ Invalid input! Please enter a valid number.") 














        

