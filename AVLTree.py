"""AVL tree implementations in python"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.balanceFactor = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node == None:
            node = Node(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        node.balanceFactor = self.height(node.left) - self.height(node.right)
        if node.balanceFactor > 1:
            if data < node.left.data:
                node = self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                node = self.rightRotate(node)
        elif node.balanceFactor < -1:
            if data > node.right.data:
                node = self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                node = self.leftRotate(node)
        return node

    def delete(self, node, data):
        if node == None:
            print("Element not found")
        elif data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left == None and node.right == None:
                node = None
            elif node.left == None or node.right == None:
                if node.left == None:
                    node = node.right
                else:
                    node = node.left
            else:
                successor = self.minValueNode(node.right)
                node.data = successor.data
                node.right = self.delete(node.right, successor.data)
        if node != None:
            node.balanceFactor = self.height(node.left) - self.height(node.right)
            if node.balanceFactor > 1:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.rightRotate(node)
                else:
                    node.left = self.leftRotate(node.left)
                    node = self.rightRotate(node)
            elif node.balanceFactor < -1:
                if self.height(node.right.right) >= self.height:
                    node = self.leftRotate(node)
                else:
                    node.right = self.rightRotate(node.right)
                    node = self.leftRotate(node)
        return node

    def minValueNode(self, right):
        current = right
        while current.left != None:
            current = current.left
        return current

    def height(self, node):
        if node == None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def rightRotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp

    def leftRotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp

    def preorder(self, node):
        if node != None:
            print(node.data, end = " ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.data, end = " ")
            self.inorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end = " ")

    def printTree(self, node, level):
        if node != None:
            self.printTree(node.right, level+1)
            print(" " * 5 * level, node.data)
            self.printTree(node.left, level+1)

def main():
    avl = AVLTree()
    print("Choose one of the following operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Preorder Traversal")
    print("4. Inorder Traversal")
    print("5. Postorder Traversal")
    print("6. Print Tree")
    print("7. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to insert: "))
            avl.root = avl.insert(avl.root, data)
        elif choice == 2:
            data = int(input("Enter data to delete: "))
            avl.root = avl.delete(avl.root, data)
        elif choice == 3:
            avl.preorder(avl.root)
            print()
        elif choice == 4:
            avl.inorder(avl.root)
            print()
        elif choice == 5:
            avl.postorder(avl.root)
            print()
        elif choice == 6:
            avl.printTree(avl.root, 0)
        elif choice == 7:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()