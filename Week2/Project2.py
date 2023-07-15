import math

# Create a tree node
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    # Function to insert a node
    def insert_node(self, root, data):
        # Find the correct location and insert the node
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
    
    # Input: An array A in sorted order, end > start > 0, and key k.
    # Output: Index i such that A[i] = k, or None if no match is found.
    def BinarySearch(self, A, start, end, k):
        m = math.floor((end + start)/2)
        if start > end:
            return None
        elif A[m] == k:
            return m
        elif A[m] > k:
            return self.BinarySearch(A, start, m-1, k)
        else:
            return self.BinarySearch(A, m+1, end, k)

    # Function to delete a node
    def delete_node(self, root, data):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)

    def printPreOrder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.data, end=" ")
        self.printInOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += " "
            else:
                print("L----", end="")
                indent += "| "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

def main():
    # myTree = AVLTree()
    # root = None
    # # THIS WILL BE REMOVED O(n)
    # data = []
    # while True:
    #     ans = int(input("Please enter a positive integer: "))
    #     if ans > 0:
    #         if ans not in data:
    #             root = myTree.insert_node(root, ans)
    #             myTree.printHelper(root, "", True)
    #             data.append(ans)
    #         else:
    #             root = myTree.delete_node(root, ans)
    #             myTree.printHelper(root, "", True)
    #             data.remove(ans)
    #     else:
    #         break


    myTree = AVLTree()
    root = None

    while True:
        ans = int(input("Please enter a positive integer: "))
        if ans > 0:
            if ans not in myTree.BinarySearch(myTree, 0, len(myTree.data)-1, ans):
                root = myTree.insert_node(root, ans)
                myTree.printHelper(root, "", True)
            else:
                root = myTree.delete_node(root, ans)
                myTree.printHelper(root, "", True)
        else:
            break


main()