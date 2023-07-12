def printPostOrder(self, root):
        if not root:
            return
        self.printPostOrder(root.left)
        self.printPostOrder(root.right)
        print(root.data, end=" ")