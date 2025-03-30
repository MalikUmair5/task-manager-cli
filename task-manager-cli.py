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
    if id < 1 or id > len(tasks):
        print("Invalid Task  Please enter a valid task Number")
        return
    try: 
        removed_task = tasks.pop(id - 1)
        if(save_tasks()):
            print(f"Task {removed_task} Deleted Successfully")
        else:
            print("Cannot Save the Task")
    except Exception as e:
        print(f"Cannot Complete Task due to {e}")

def show_all_tasks():
    if not tasks:
        print("No Tasks are available")
        return
    i = 1
    print("\n")
    for task in tasks:
        print(f"{i}) {task["Title"]} [{task["Status"]}]")
        i += 1
    print("\n")

def mark_as_done(id):
    try:
        tasks[id -1]["Status"] = "Completed"
        if save_tasks():
            print("Task Saved Successfully")
        else: 
            print("Connot Save the task")
    except Exception as e:
        print(f"Cannot Mark as done due to {e}")

def save_tasks():
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
            return True
    except Exception as e:
        print(f"Error Saving Tasks {e}")
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
                try:
                    id = int(input("Enter Task Number To Delete: "))
                    remove_task(id)
                except ValueError:
                    print("Please Enter a valid Input")
                print("\n")

            elif selected_Option == 3:
                print("\n")
                show_all_tasks()
                print("\n")
                try:
                    id = int(input("Enter Task Number To Mark as Done: "))
                    mark_as_done(id)
                except ValueError:
                    print("Please Enter a valid input")
                print("\n")

            elif selected_Option == 4:
                show_all_tasks()
            elif selected_Option == 5:
                break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
            print("❌ Invalid input! Please enter a valid number.") 














        

