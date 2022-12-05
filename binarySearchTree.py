"""binary search tree implementation in python"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):
        if None == self.root:
            self.root = Node(data)
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left == None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right
        return self.root


    def deleteElement(self, data):
        if self.root == None:
            print("Tree is empty")
        else:
            temp = self.root
            while temp != None:
                if data < temp.data:
                    prev = temp
                    temp = temp.left
                elif data > temp.data:
                    prev = temp
                    temp = temp.right
                else:
                    #if node to be deleted is leaf node
                    if temp.left == None and temp.right == None:
                        if prev.left == temp:
                            prev.left = None
                        else:
                            prev.right = None
                    #if node to be deleted has only one child
                    elif temp.left == None or temp.right == None:
                        if temp.left == None:
                            if prev.left == temp:
                                prev.left = temp.right
                            else:
                                prev.right = temp.right
                        else:
                            if prev.left == temp:
                                prev.left = temp.left
                            else:
                                prev.right = temp.left
                    #if node to be deleted has both children
                    else:
                        successor = self.minValueNode(temp.right)
                        temp.data = successor.data
                        self.deleteElement(successor.data)
                    break
        return self.root

    def postOrderTraversal(self, root):
        if root == None:
            print("Tree is Empty.")
        else:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data)

    def preOrderTraversal(self, root):
        if root == None:
            print("Tree is Empty.")
        else:
            print(root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def inOrderTraversal(self, root):
        if root == None:
            print("Tree is Empty.")
        else:
            self.inOrderTraversal(root.left)
            print(root.data)
            self.inOrderTraversal(root.right)

    def minValueNode(self, right):
        current = right
        while current.left != None:
            current = current.left
        return current

    def maxValueNode(self, left):
        current = left
        while current.right != None:
            current = current.right
        return current

    #finding hight of tree
    def height(self, root):
        if root == None:
            return 0
        else:
            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)
            if leftHeight > rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1

    def printTree(self, node, level):
        if node != None:
            self.printTree(node.right, level+1)
            print(" " * 5 * level, node.data)
            self.printTree(node.left, level+1)


def main():
    bst = BinarySearchTree()
    print("Choose one of the following operations:")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Post order traversal")
    print("4. Pre order traversal")
    print("5. In order traversal")
    print("6. Print tree")
    print("7. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the element: "))
            bst.insertElement(data)
        elif choice == 2:
            data = int(input("Enter the element: "))
            bst.deleteElement(data)
        elif choice == 3:
            bst.postOrderTraversal(bst.root)
        elif choice == 4:
            bst.preOrderTraversal(bst.root)
        elif choice == 5:
            bst.inOrderTraversal(bst.root)
        elif choice == 6:
            bst.printTree(bst.root, 0)
        elif choice == 7:
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()