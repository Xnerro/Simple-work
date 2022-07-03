class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.data < data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            else:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)

    def inorder(self):
        if self:
            Tree.inorder(self.left)
            print(self.data)
            Tree.inorder(self.right)

    def preorder(self):
        if self:
            print(self.data)
            Tree.preorder(self.left)
            Tree.preorder(self.right)

    def postorder(self):
        if self:
            Tree.postorder(self.left)
            Tree.postorder(self.right)
            print(self.data)


# initial new tree

root = Tree(10)
root.insert(5)
root.insert(11)
root.insert(8)


root.preorder()
