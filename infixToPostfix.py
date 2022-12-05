"""converting infix to postfix using stack"""

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
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i], end='-')


def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return -1

def infixToPostfix(string):
    stack = Stack()
    postfix = ''
    for i in range(len(string)):
        if string[i].isalnum():
            postfix += string[i]
        elif string[i] == '(':
            stack.push(string[i])
        elif string[i] == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                postfix += stack.peek()
                stack.pop()
            if stack.isEmpty() and stack.peek() != '(':
                print("Invalid expression")
                return -1
            else:
                stack.pop()
        else:
            while not stack.isEmpty() and precedence(string[i]) < precedence(stack.peek()):
                postfix += stack.peek()
                stack.pop()
            stack.push(string[i])
    while not stack.isEmpty():
        postfix += stack.peek()
        stack.pop()
    return postfix

def main():
    string = input("Enter the expression: ")
    print(infixToPostfix(string))


if __name__ == '__main__':
    main()
