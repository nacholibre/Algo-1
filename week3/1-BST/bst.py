class BST:

    # Checks if a binary tree is a binary search tree.
    # root - node with `left`, `right` and `value` properties
    def isBST(self, root):
        pass


class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


if __name__ == '__main__':
    mylist = [15, 20, 1, 30, 40, 100, 6, 3]

    currentIndex = 0

    node = Node()
    node.value = mylist.pop(0)

    root = node
