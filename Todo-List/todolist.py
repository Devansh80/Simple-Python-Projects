# Define a TodoList class that represents a task list
class TodoList:
    # Constructor method to initialize the TodoList object with an empty task list
    def __init__(self):
        self.tasks = []
    
    # Method to add a task to the task list    
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")
    
    # Method to remove a task from the task list
    def remove_task(self, task):
        # Check if the task is present in the task list
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")
    
    # Method to display all the tasks in the task list        
    def display_tasks(self):
        print("Task List:")
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print("No tasks found.")

            
# Define a main function that uses the TodoList class to create a task list and interact with it
def main():
    # Create a new TodoList object
    todo_list = TodoList()
    # Display a menu and accept user input until the user chooses to exit
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        # Call the add_task method if the user chooses to add a task
        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        # Call the remove_task method if the user chooses to remove a task
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        # Call the display_tasks method if the user chooses to display all tasks
        elif choice == "3":
            todo_list.display_tasks()
        # Exit the program if the user chooses to exit
        elif choice == "4":
            print("Goodbye!")
            break
        # Display an error message if the user enters an invalid choice
        else:
            print("Invalid choice. Please try again.")

# Call the main function.
if __name__ == '__main__':
    main()

