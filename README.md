# 📝 Task Manager CLI

A simple command-line task manager written in Python. It lets you add, update, delete, mark, and filter tasks. Your tasks are saved to a JSON file and automatically loaded next time you run the app. Includes color-coded terminal output using `colorama`.

---

## 🚀 Features

- ✅ Add tasks with descriptions
- ✏️ Update descriptions and status
- 🔄 Change task status to:
  - `todo`
  - `in-progress`
  - `done`
- ❌ Remove tasks by ID
- 📋 List all tasks or filter by status (`list done`, `list todo`, etc.)
- 💾 Tasks persist between runs (saved in `tasks.json`)

## 🧰 Requirements

- Python 3.6+
- `colorama` package

Install it with:

```bash
pip install colorama
```
🛠️ How to Use


Run the script from your terminal:
```bash

python main.py
```

🧪 Example
```bash


Welcome to the Task Manager CLI!
Enter a command: add
Enter the new task: Finish the project
Task added with ID 1

Enter a command: list
Your tasks:
ID: 1, Desc: Finish the project, Status: todo

Enter a command: mark-done
Enter the ID of the task to mark done: 1
Task ID 1 marked as done.

Enter a command: list done
Your tasks:
ID: 1, Desc: Finish the project, Status: done
```
