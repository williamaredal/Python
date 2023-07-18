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
        parent_node = self.root

        # if tree is empty, insert number at root node
        if  parent_node.data == None:
            parent_node.data = number
            return

        while True:
            # should insert number left if less than parent node
            if number < parent_node.data:
                if parent_node.left_branch == None:
                    parent_node.left_branch = Node(data=number)
                    return
                # moves to next node on left side if it's not empty
                parent_node = parent_node.left_branch

        # should insert number right if bigger than parent node
            else:
                if parent_node.right_branch == None:
                    parent_node.right_branch = Node(data=number)
                    return
                # moves to next node on right side if it's not empty
                parent_node = parent_node.right_branch


    def search(self, number):
        # navigates the tree using the same rules as when inserting
        return None
