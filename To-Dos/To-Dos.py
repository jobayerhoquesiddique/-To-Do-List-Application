import json

class Node():
    """ 
    @description: This class will act as node for To-Do List and will hold data.
    previous_node: a pointer, indicates the address of previous node.
    next_node: a pointer, indicates the address of next node.
    """
    def __init__(self, item=None, previous_node=None, next_node=None):
        self.item = item
        self.previous_node = previous_node
        self.next_node = next_node

class ToDoListApplication():
    """
    @description: This class defines several methods for the To-Do List Application.
    params:
        head: indicates the first node of the list.
        tail: indicates the last node of the list.
    """
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def appendleft(self, item):
        # Adds an item to the head of the list
        new_node = Node(item)
        new_node.previous_node = None
        new_node.next_node = self.head
        if self.head is None:
            self.tail = new_node
        else:
            self.head.previous_node = new_node
        self.head = new_node

    def append(self, item):
        # Adds an item to the end of the list
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.previous_node = self.tail
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node

    def insert(self, position, item):
        # Adds an item to an exact position of the list
        if position == 0:
            self.appendleft(item)
            print(item, "inserted to position", position)
        elif position == self.size():
            self.append(item)
            print(item, "inserted to position", position)
        elif position > self.size():
            print("Error: Position out of range")
            return False
        else:
            current = self.head
            index = 0
            while current:
                if index != position:
                    previous = current
                    current = current.next_node
                    index += 1
                else:
                    new_node = Node(item, previous, current)
                    previous.next_node = new_node
                    current.previous_node = new_node
                    print(item, "inserted to position", position)
                    break
        return True

    def is_empty(self):
        # Checks whether the list is empty or not
        return self.head is None

    def size(self):
        # Returns the total number of items in the list
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def search(self, item):
        # Checks whether an item exists in the list or not
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next_node
        print("Item not found")
        return False

    def remove(self, item):
        # Removes an item from the list
        if self.is_empty():
            print("Empty List")
            return
        current = self.head
        previous = None
        while current:
            if current.item == item:
                if previous is None:
                    self.popleft()
                else:
                    previous.next_node = current.next_node
                    if current.next_node:
                        current.next_node.previous_node = previous
                    else:
                        self.tail = previous
                    print(item, "removed")
                return
            previous = current
            current = current.next_node
        print("Item not found")

    def popleft(self):
        # Removes an item from the head of the list
        if self.is_empty():
            print("List is empty!")
            return
        removed_item = self.head.item
        self.head = self.head.next_node
        if self.head:
            self.head.previous_node = None
        else:
            self.tail = None
        print(removed_item, "removed from the list.")

    def printlist(self):
        # Prints all tasks in the list
        if self.is_empty():
            print("Empty List")
        else:
            current = self.head
            while current:
                print(current.item)
                current = current.next_node

    def export_tasks(self, filename="tasks.json"):
        # Exports tasks to a JSON file
        tasks = []
        current = self.head
        while current:
            tasks.append({"item": current.item})
            current = current.next_node
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=4)
        print("Tasks exported successfully to", filename)

    def import_tasks(self, filename="tasks.json"):
        # Imports tasks from a JSON file and appends them to the list
        try:
            with open(filename, "r") as f:
                tasks = json.load(f)
            for task in tasks:
                self.append(task["item"])
            print("Tasks imported successfully from", filename)
        except FileNotFoundError:
            print("File not found!")

def main():
    # Main function for the CLI version of the To-Do List Application
    mylist = ToDoListApplication()
    while True:
        print("\nTo-Do List Application")
        print("\nFeatures:")
        print("1. Add Task")
        print("2. Insert Task")
        print("3. Get Size")
        print("4. Search Task")
        print("5. Remove Task")
        print("6. Show List")
        print("7. Export Tasks")
        print("8. Import Tasks")
        print("9. Quit")
        try:
            case = int(input("\nWhat do you wanna do? "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if case == 1:
            item = input("Input task you want to add to the list: ")
            mylist.appendleft(item)
            print("Congrats!", item, "has been added")
        elif case == 2:
            try:
                position = int(input("Input position: "))
                if position < 0:
                    print("Error: Position cannot be negative!")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
            item = input("Input task you want to insert: ")
            success = mylist.insert(position, item)
            if success:
                print("Congrats!", item, "has been inserted")
        elif case == 3:
            print("There are", mylist.size(), "tasks in the list")
        elif case == 4:
            item = input("Input task you want to search for: ")
            found = mylist.search(item)
            if found:
                print("Task", item, "found")
        elif case == 5:
            if mylist.is_empty():
                print("Empty List")
            else:
                item = input("Input task you want to remove: ")
                mylist.remove(item)
        elif case == 6:
            mylist.printlist()
        elif case == 7:
            mylist.export_tasks()
        elif case == 8:
            mylist.import_tasks()
        elif case == 9:
            print("The app is quitting.")
            break
        else:
            print("Oops! Wrong Choice. Please try again.")

if __name__ == "__main__":
    main()
