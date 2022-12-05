"""Reversing a string using stack"""

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

def reverseString(string):
    stack = Stack()
    for i in range(len(string)):
        stack.push(string[i])
    reverse = ''
    while not stack.isEmpty():
        reverse += stack.peek()
        stack.pop()
    return reverse

def main():
    string = input("Enter the string to be reversed: ")
    print(reverseString(string))

if __name__ == '__main__':
    main()