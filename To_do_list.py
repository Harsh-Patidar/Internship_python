class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.description}")
            if task.due_date:
                print(f"   Due Date: {task.due_date}")
            if task.priority:
                print(f"   Priority: {task.priority}")
            print()

    def display_completed_tasks(self):
        print("\nCompleted Tasks:")
        for i, task in enumerate(self.completed_tasks, start=1):
            print(f"{i}. {task.description}")

    def mark_task_completed(self, task_index):
        task = self.tasks.pop(task_index - 1)
        task.completed = True
        self.completed_tasks.append(task)
        print(f'Task "{task.description}" marked as completed.')

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        task = self.tasks[task_index - 1]
        task.description = new_description
        task.due_date = new_due_date
        task.priority = new_priority
        print('Task updated successfully.')

    def remove_task(self, task_index):
        removed_task = self.tasks.pop(task_index - 1)
        print(f'Task "{removed_task.description}" removed from the list.')

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Display Completed Tasks")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)
            print('Task added successfully.')
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            new_description = input("Enter new description: ")
            new_due_date = input("Enter new due date (optional): ")
            new_priority = input("Enter new priority (optional): ")
            todo_list.update_task(task_index, new_description, new_due_date, new_priority)
        elif choice == "5":
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "6":
            todo_list.display_completed_tasks()
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
