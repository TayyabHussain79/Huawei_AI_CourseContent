# TO-DO List Application
class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} - {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        """Add a new task to the list"""
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        """Display all tasks with their status"""
        if not self.tasks:
            print("No tasks found!")
            return

        print("\nYour To-Do List:")
        print("-" * 40)
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")
        print("-" * 40)

    def mark_task_complete(self, task_index):
        """Mark a task as complete"""
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_completed()
            print(f"Task '{task.title}' marked as complete!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_index):
        """Delete a task from the list"""
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task.title}' deleted successfully!")
        else:
            print("Invalid task number!")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            todo_list.add_task(title, description)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_num = input("Enter task number to mark as complete: ")
            if task_num.isdigit():
                todo_list.mark_task_complete(int(task_num))
            else:
                print("Please enter a valid number!")

        elif choice == "4":
            todo_list.view_tasks()
            task_num = input("Enter task number to delete: ")
            if task_num.isdigit():
                todo_list.delete_task(int(task_num))
            else:
                print("Please enter a valid number!")

        elif choice == "5":
            print("Thank you for using the To-Do List application!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()