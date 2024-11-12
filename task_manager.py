import json

# Define the Task class
class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.task_id}, title='{self.title}', completed={self.completed})"

# Function to add a task
def add_task(title):
    task_id = len(tasks) + 1
    tasks.append(Task(task_id, title))
    print(f"Task '{title}' added successfully with ID: {task_id}")

# Function to view all tasks
def task_view():
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"[{task.task_id}] {task.title} - {status}")

# Function to delete a task by ID
def delete_task(task_id):
    global tasks
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted successfully.")
            return
    print(f"Task {task_id} not found.")

# Function to mark a task as completed
def mark_completed(task_id):
    for task in tasks:
        if task.task_id == task_id:
            task.completed = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

# Function to save tasks to a JSON file
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([task.__dict__ for task in tasks], f)
    print("Tasks saved successfully.")


# Initialize the tasks list
tasks = []
# Function to load tasks from a JSON file
def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as f:
            tasks_data = json.load(f)
            tasks = [Task(task_id=task['task_id'], title=task['title'], completed=task['completed']) for task in tasks_data]
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No tasks available to load.")

# CLI menu display function
def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")
    return int(input("Enter your choice: "))


# Dummy login credentials for testing
DUMMY_EMAIL = "user@example.com"
DUMMY_PASSWORD = "test123"

# Dummy Login Function
def login():
    print("Welcome to the Task Manager CLI!")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False


# Main function to run the task manager
def main():
    # Login loop until successful login
    while not login():
        pass
    
    print("Welcome to the Task Manager!")  # Starting message
    load_tasks()  # Load tasks when the application starts
    while True:
        choice = show_menu()
        if choice == 1:
            add_task(input("Enter task title: "))
        elif choice == 2:
            task_view()
        elif choice == 3:
            delete_task(int(input("Enter task ID to delete: ")))
        elif choice == 4:
            mark_completed(int(input("Enter task ID to mark as completed: ")))
        elif choice == 5:
            save_tasks()
        elif choice == 6:
            load_tasks()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
