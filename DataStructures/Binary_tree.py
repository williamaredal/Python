class Node:
    def __init__(self, parent=None, data=None, original_index=None, left_branch=None, right_branch=None):
        self.parent = parent,
        self.data = data
        self.original_index = original_index
        self.left_branch = left_branch
        self.right_branch = right_branch


class BinaryTree:
    def __init__(self, root_data=None):
        self.root = Node(data=root_data)

    def insert(self, number):
        # checks which leaf node (left/right) to insert number. Left if less than current node value, right if bigger
        return None

    def search(self, numeber):
        # navigates the tree using the same rules as when inserting
        return None
