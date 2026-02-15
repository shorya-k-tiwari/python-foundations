"""
To-Do List Manager

Functions:
- add_task()
- view_tasks()
- mark_done()
"""

tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task cannot be empty")
        return
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print("Task added")

def view_tasks():
    if not tasks:
        print("No tasks available")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a valid number")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Exit")

        choice = input("Choose: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()