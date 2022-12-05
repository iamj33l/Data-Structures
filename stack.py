"""stack implementation in python"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def printStack(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i], end='-')

def main():
    stack = Stack()
    print("Choose from the option below: ")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Peek an element")
    print("4. Print the stack")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            data = int(input("Enter the element to be pushed: "))
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            print(stack.peek())
        elif choice == 4:
            stack.printStack()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
        choice = int(input("Enter your choice: "))

if __name__ == '__main__':
    main()