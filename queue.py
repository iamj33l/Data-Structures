"""Queue implementation in python"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def printQueue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            for i in range(len(self.queue)):
                print(self.queue[i], end='-')

def main():
    queue = Queue()
    print("Choose from the option below: ")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Peek an element")
    print("4. Print the queue")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            data = int(input("Enter the element to be enqueued: "))
            queue.enqueue(data)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            print(queue.peek())
        elif choice == 4:
            queue.printQueue()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
        choice = int(input("Enter your choice: "))

if __name__ == '__main__':
    main()