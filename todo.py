# Define a class to represent a to-do list item
class TodoItem:
    def __init__(self, title):
        self.title = title
        self.completed = False

# Define a class to represent the to-do list itself
class TodoList:
    def __init__(self):
        self.items = []

    # Method to add a new item to the list
    def add_item(self, title):
        self.items.append(TodoItem(title))
        print("Task added successfully!")

    # Method to mark an item as completed
    def complete_item(self, index):
        if 0 <= index < len(self.items):
            self.items[index].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    # Method to remove an item from the list
    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

    # Method to display all items in the list
    def display_items(self):
        if len(self.items) == 0:
            print("No tasks in the list.")
        else:
            print("ToDo List:")
            for i, item in enumerate(self.items):
                status = "Completed" if item.completed else "Pending"
                print(f"{i + 1}. [{status}] {item.title}")


# Function to display menu options
def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View Tasks")
    print("5. Exit")


# Main function
def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            todo_list.add_item(title)
        elif choice == "2":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.complete_item(index)
        elif choice == "3":
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_item(index)
        elif choice == "4":
            todo_list.display_items()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
