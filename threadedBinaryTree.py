"""threaded binary tree implementation in python"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.lthread = True
        self.rthread = True

class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        ptr = self.root
        prev = None
        while ptr != None:
            prev = ptr
            if data < ptr.data:
                if ptr.lthread == False:
                    ptr = ptr.left
                else:
                    break
            else:
                if ptr.rthread == False:
                    ptr = ptr.right
                else:
                    break

        temp = Node(data)
        if prev == None:
            self.root = temp
            temp.left = None
            temp.right = None
        elif data < prev.data:
            temp.left = prev.left
            temp.right = prev
            prev.lthread = False
            prev.left = temp
        else:
            temp.left = prev
            temp.right = prev.right
            prev.rthread = False
            prev.right = temp

        return self.root

    def inOrderSuccessor(self, node):
        if node.rthread == True:
            return node.right
        else:
            node = node.right
            while node.lthread == False:
                node = node.left
            return node

    def delete(self, data):
        ptr = self.root
        prev = None
        while ptr != None:
            if data < ptr.data:
                prev = ptr
                ptr = ptr.left
            elif data > ptr.data:
                prev = ptr
                ptr = ptr.right
            else:
                break

        if ptr == None:
            print("Node not found")
            return

        if ptr.lthread == True and ptr.rthread == True:
            if prev == None:
                self.root = None
            elif ptr == prev.left:
                prev.left = ptr.left
                prev.lthread = True
            else:
                prev.right = ptr.right
                prev.rthread = True
        elif ptr.lthread == False and ptr.rthread == True:
            if prev == None:
                self.root = ptr.left
            elif ptr == prev.left:
                prev.left = ptr.left
            else:
                prev.right = ptr.left
        elif ptr.lthread == True and ptr.rthread == False:
            if prev == None:
                self.root = ptr.right
            elif ptr == prev.left:
                prev.left = ptr.right
            else:
                prev.right = ptr.right
        else:
            temp = self.inOrderSuccessor(ptr)
            if prev == None:
                self.root = temp
            elif ptr == prev.left:
                prev.left = temp
            else:
                prev.right = temp
            temp.left = ptr.left
        return self.root

    def inOrder(self):
        if self.root == None:
            print("Tree is empty")
        else:
            temp = self.root
            while temp.lthread == False:
                temp = temp.left
            while temp != None:
                print(temp.data, end=" ")
                temp = self.inOrderSuccessor(temp)
        print()

    def printTree(self, node, level):
        if node != None:
            self.printTree(node.right, level+1)
            print(" " * 5 * level, node.data)
            self.printTree(node.left, level+1)

def main():
    tbt = ThreadedBinaryTree()
    print("Choose one of the following operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Inorder traversal")
    print("4. Print tree")
    print("4. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data: "))
            tbt.insert(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            tbt.delete(data)
        elif choice == 3:
            tbt.inOrder()
        elif choice == 4:
            tbt.printTree(tbt.root, 0)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()