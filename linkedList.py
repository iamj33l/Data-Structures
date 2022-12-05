"""linked list implementation in python"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None;

    def createList(self):
        status = True
        while status:
            data = int(input("Enter the element: "))
            self.insertAtEnd(data)
            choice = input("Do you want to continue? (y/n): ")
            if choice == 'n':
                status = False

    def insertAtBeginning(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def insertAtEnd(self, data):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def insertAtPosition(self, data, position):
        temp = self.head
        for i in range(position-2):
            temp = temp.next
        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode

    def deleteAtBeginning(self):
        temp = self.head
        self.head = temp.next
        temp = None

    def deleteAtEnd(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def deleteAtPosition(self, position):
        temp = self.head
        for i in range(position-2):
            temp = temp.next
        temp.next = temp.next.next

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end='->')
            temp = temp.next
        print("None", end='')

    def reverseList(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

def main():
    linkedList = LinkedList()
    print("Choose from the options below:")
    print("1. Insert")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at position")
    print("5. Delete at beginning")
    print("6. Delete at end")
    print("7. Delete at position")
    print("8. Print list")
    print("9. Reverse list")
    print("10. Exit")
    choice = int(input("Enter your choice: "))

    while choice != 10:
        if choice == 1:
            data = int(input("Enter data: "))
            linkedList.insert(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            linkedList.insertAtBeginning(data)
        elif choice == 3:
            data = int(input("Enter data: "))
            linkedList.insertAtEnd(data)
        elif choice == 4:
            data = int(input("Enter data: "))
            position = int(input("Enter position: "))
            linkedList.insertAtPosition(data, position)
        elif choice == 5:
            linkedList.deleteAtBeginning()
        elif choice == 6:
            linkedList.deleteAtEnd()
        elif choice == 7:
            position = int(input("Enter position: "))
            linkedList.deleteAtPosition(position)
        elif choice == 8:
            linkedList.printList()
        elif choice == 9:
            linkedList.reverseList()
        else:
            print("Invalid choice")
        choice = int(input("\nEnter your choice: "))

if __name__ == "__main__":
    main()