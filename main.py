import datetime
tasks = []
next_id=1 
def mark_in_progress(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = get_current_time()
            print(f"Task ID {task_id} marked as in-progress.")
            return
    print("No task found with that ID.")

def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = get_current_time()
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
    else:
        print("No task entered. Try again.")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for task in tasks:
            print(f"ID: {task['id']}, Desc: {task['description']}, Status: {task['status']}")

def main():
    print("Welcome to the Task Manager CLI!")
    while True:
        command = input('''Enter a command 
            - add 
             - list
              - remove
               - update
                - mark-in-progress
                 - mark-done
                  - exit
             ''').strip().lower()

        if command == "add":
            add_task()
        elif command == "list":
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
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
