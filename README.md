# Task Manager (Python)

A simple **Task Manager** built using Python that allows users to **add, remove, mark tasks as done, and view all tasks**. Tasks are saved in a JSON file to maintain persistence.

## Features
- ✅ **Add Tasks**
- ❌ **Remove Tasks**
- 📋 **View All Tasks**
- ✅ **Mark Tasks as Done**
- 💾 **Persistent Storage using JSON**

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```
2. **Run the Script**
   ```sh
   python task_manager.py
   ```

## Usage
Once you run the script, you will see the following menu:
```
====== 📝 Task Manager ======
1. ➕ Add a Task
2. ❌ Remove a Task
3. ✅ Mark a Task as Done
4. 📋 List All Tasks
5. 🔴 Exit
```

### 1️⃣ Adding a Task
Enter **1** and type the task you want to add. Example:
```
Enter the task to add: Buy groceries
✔️ Task Added Successfully!
```

### 2️⃣ Removing a Task
Enter **2**, see the list of tasks, and enter the **task number** to delete it.
```
Enter Task Number to Delete: 1
✔️ Task 'Buy groceries' Deleted Successfully!
```

### 3️⃣ Marking a Task as Done
Enter **3**, see the list of tasks, and enter the **task number** to mark it as done.
```
Enter Task Number to Mark as Done: 2
✔️ Task Marked as Done!
```

### 4️⃣ Viewing All Tasks
Enter **4** to list all tasks.
```
📋 Your Tasks:
1) Buy groceries [Completed]
2) Finish Python project [Pending]
```

### 5️⃣ Exiting
Enter **5** to exit.
```
👋 Exiting Task Manager. Goodbye!
```

## File Storage
- All tasks are stored in **tasks.json** file.
- If the file does not exist, it will be created automatically.
- If the file is corrupted, a new file will be created.

## Requirements
- **Python 3.x**

## License
This project is **free to use**. Modify and improve as needed!

---

**Happy Coding! 🚀**

