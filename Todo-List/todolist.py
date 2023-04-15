class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")
        
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")
            
    def display_tasks(self):
        print("Task List:")
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print("No tasks found.")
            
def main():
    todo_list = TodoList()
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

