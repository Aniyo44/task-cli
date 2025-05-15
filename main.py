import datetime
import os 
import json 
TASKS_FILE = "tasks.json"

tasks = []
next_id=1 

def load_tasks():
    global tasks, next_id
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                tasks_data = json.load(f)
                tasks = tasks_data.get("tasks", [])
                next_id = tasks_data.get("next_id", 1)
            except json.JSONDecodeError:
                print("Error reading tasks.json. Starting with an empty task list.")
                tasks = []
                next_id = 1
    else:
        tasks = []
        next_id = 1 
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump({
            "tasks": tasks,
            "next_id": next_id
        }, f, indent=4)

def mark_todo(task_id):
    for task in tasks:
        if task["id"]== task_id:
            task["status"]="todo"
            task["updatedAt"] = get_current_time()
            save_tasks() 
            print(f"Task ID {task_id} todo.")
            return
    print("NO task found with that ID.")    



def mark_in_progress(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = get_current_time()
            save_tasks() 
            print(f"Task ID {task_id} marked as in-progress.")
            return
    print("No task found with that ID.")

def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = get_current_time()
            save_tasks() 
            print(f"Task ID {task_id} marked as done.")
            return
    print("No task found with that ID.")
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def update_task():
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        for task in tasks:
            if task["id"] == task_id:
                new_description = input("Enter the new description: ").strip()
                new_status = input("Enter the new status (todo, in-progress, done): ").strip().lower()
                if new_description:
                    task["description"] = new_description
                if new_status in ["todo", "in-progress", "done"]:
                    task["status"] = new_status
                task["updatedAt"] = get_current_time()
                save_tasks() 
                print(f"Updated task ID {task_id}")
                return
        print("No task found with that ID.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    try:
        task_id = int(input("Enter the ID of the task to remove: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks() 
                print(f"Removed task ID {task_id}")
                return
        print("No task found with that ID.")
    except ValueError:
        print("Please enter a valid number.")


def add_task():
    global next_id

    description = input("Enter the new task: ").strip()
    if description:
        task={
            "id": next_id,
            "description": description,
            "status": "todo",
            "createdAt": get_current_time(),
            "updatedAt": get_current_time()
        }
        tasks.append(task)

        print(f"Task added with ID {next_id}")
        next_id += 1
        save_tasks() 
    else:
        print("No task entered. Try again.")


def show_tasks(status_filter=None):
    filtered_tasks = tasks if status_filter is None else [task for task in tasks if task["status"] == status_filter]

    if not filtered_tasks:
        print("No tasks found." if status_filter else "No tasks yet.")
    else:
        print("Your tasks:" if status_filter is None else f"Your {status_filter} tasks:")
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Desc: {task['description']}, Status: {task['status']}")

def main():
    load_tasks()
    print("Welcome to the Task Manager CLI!")
    while True:
        command = input('''Enter a command 
            - add 
             - list(add their status to filter ex : list done/ list todo)
              - remove
               - update
                - mark-in-progress / mark-done / mark-todo
                  - exit
             ''').strip().lower()

        if command == "add":
            add_task()
        elif command == "list":
            show_tasks()
        elif command.startswith("list"):
            parts = command.split()
            if len(parts) == 2 and parts[1] in ["todo", "in-progress", "done"]:
                show_tasks(parts[1])
            else:
                show_tasks()
        elif command == "update":
            update_task()
        elif command=="remove":
            remove_task()
        elif command.startswith("mark-in-progress"):
            try:
                task_id = int(input("Enter the ID of the task to mark in-progress: "))
                mark_in_progress(task_id)
            except ValueError:
                print("Invalid ID.")
        elif command.startswith("mark-done"):
            try:
                task_id = int(input("Enter the ID of the task to mark done: "))
                mark_done(task_id)
            except ValueError:
                print("Invalid ID.")
        elif command.startswith("mark-todo"):
            try:
                task_id = int(input("Enter the ID of the task to mark todo: "))
                mark_todo(task_id)
            except ValueError:
                print("Invalid ID.")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
