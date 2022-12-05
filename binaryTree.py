"""binary tree implementation in python"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    #insert element using queue in binary tree
    def insertElement(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            queue = []
            queue.append(self.root)
            while len(queue) != 0:
                temp = queue.pop(0)
                if temp.left != None:
                    queue.append(temp.left)
                else:
                    temp.left = Node(data)
                    break
                if temp.right != None:
                    queue.append(temp.right)
                else:
                    temp.right = Node(data)
                    break

    def deleteDeepest(self, node):
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            temp = queue.pop(0)
            if temp == node:
                temp = None
                return
            if temp.right:
                if temp.right == node:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
            if temp.left:
                if temp.left == node:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)

    #delete element using queue in binary tree
    def deleteElement(self, data):
        if self.root == None:
            print("Tree is empty")
        if self.root.left == None and self.root.right == None:
            if self.root.data == data:
                root = None
            else:
                print("Element not found")
        node = None
        queue = []
        queue.append(self.root)
        temp = None
        while len(queue) != 0:
            temp = queue.pop(0)
            if temp.data == data:
                node = temp
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        if node != None:
            x = temp.data
            self.deleteDeepest(temp)
            node.data = x
        return self.root

    def preOrder(self, node):
        if node != None:
            print(node.data, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print(node.data, end=' ')
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=' ')

    #print element in tree design
    def printTree(self, node, level):
        if node != None:
            self.printTree(node.right, level+1)
            print(" " * 5 * level, node.data)
            self.printTree(node.left, level+1)

def main():
    tree = BinaryTree()
    print("Choose one of the following operations:")
    print("1. Insert element")
    print("2. Delete element")
    print("3. Preorder traversal")
    print("4. Inorder traversal")
    print("5. Postorder traversal")
    print("6. Print tree")
    print("7. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to insert: "))
            tree.insertElement(data)
        elif choice == 2:
            data = int(input("Enter data to delete: "))
            tree.deleteElement(data)
        elif choice == 3:
            tree.preOrder(tree.root)
            print()
        elif choice == 4:
            tree.inOrder(tree.root)
            print()
        elif choice == 5:
            tree.postOrder(tree.root)
            print()
        elif choice == 6:
            tree.printTree(tree.root, 0)
        elif choice == 7:
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()