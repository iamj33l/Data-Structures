"""Checking nesting of parentheses, in an expression using stack"""

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

def checkParentheses(string):
    stack = Stack()
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            stack.push(string[i])
        elif string[i] == ')' or string[i] == '}' or string[i] == ']':
            if stack.isEmpty():
                return False
            else:
                if string[i] == ')' and stack.peek() == '(':
                    stack.pop()
                elif string[i] == '}' and stack.peek() == '{':
                    stack.pop()
                elif string[i] == ']' and stack.peek() == '[':
                    stack.pop()
                else:
                    return False
    return stack.isEmpty()

def main():
    string = input("Enter the expression: ")
    if checkParentheses(string):
        print("Expression is valid")
    else:
        print("Expression is invalid")

if __name__ == '__main__':
    main()