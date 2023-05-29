import math

def Binary_Search(element_list, desired_element):
    # sets the bounding indexes used to select middle element by index
    left_index = 0
    right_index = len(element_list) -1
    mid_index = right_index // 2
    search_count = 1
    search_limit = round(math.log2(len(element_list))) 

    # starts the search while avoiding eternal loop using search_limit to stop
    while search_count < search_limit:
        if element_list[mid_index] == desired_element:
            print('Found element at index: ', mid_index, 'after ', search_count, 'lookups')
            return mid_index

        ### if the middle element is not equal to the desired_element, it checks if it go left/right
        # if the middle element is higher than the desired_element, it moves mid_index to the middle of mid_index and left_index
        elif element_list[mid_index] > desired_element:
            new_mid_index = (left_index + mid_index) // 2
            mid_index = new_mid_index

        # if the middle element is higher than the desired_element, it moves mid_index to the middle of mid_index and right_index
        elif element_list[mid_index] < desired_element:
            new_mid_index = (right_index + mid_index) // 2
            mid_index = new_mid_index

        search_count += 1


    # did not find the desired_element in the element_list
    print('Could not find the desired_element in the element list after ', search_count, 'lookups')
    return -1


'''
    R
   / \
  l   r
'''
class Node:
    def __init__(self, parent=None, data=None, original_index=None, left_branch=None, right_branch=None):
        self.parent = parent,
        self.data = data
        self.original_index = original_index
        self.left_branch = left_branch
        self.right_branch = right_branch


    
def Binary_Tree_Insertion(unsorted_list, verbose=False):
    # the tree that will store the sorted values
    binary_tree = Node(
        parent=None,
        data=None,
        original_index=None,
        left_branch=None,
        right_branch=None
    )

    # Iterates over each element in the unsorted list and inserts them into the binary tree structure following these rules:
    # - if the element is larger than the root node, it's inserted as a right branch
    # - if the element is less than the root node, it's inserted as a left branch
    for index, element in enumerate(unsorted_list):
        inserted = False

        current_node = binary_tree
        while inserted == False:
            # inserts the first element (the root node)
            if index == 0:
                current_node.data = element
                current_node.original_index = index
                inserted = True
                if verbose == True:
                    print('Root node:', current_node.data)
                    print()

                continue
            

            ### Right branch
            # if right branch is filled, change current node to this and continue the comparrison
            elif element > current_node.data and current_node.right_branch != None:
                if verbose == True:
                    print(element, ', moved left')
                    print('Current node:', current_node.data)
                    print('Left branch:', current_node.left_branch.data if current_node.left_branch != None else 'None')
                    print('Rigth branch:', current_node.right_branch.data if current_node.right_branch != None else 'None')
                    print()

                current_node = current_node.right_branch
                continue

            # if the element is larger than the parent node, place it to the right
            elif element > current_node.data and current_node.right_branch == None:
                current_node.right_branch = Node(
                    parent=current_node,
                    data=element,
                    original_index=index,
                    left_branch=None,
                    right_branch=None
                )
                inserted = True
                if verbose == True:
                    print('inserted', element, 'right')
                    print('Current node:', current_node.data)
                    print('Left branch:', current_node.left_branch.data if current_node.left_branch != None else 'None')
                    print('Rigth branch:', current_node.right_branch.data if current_node.right_branch != None else 'None')
                    print()
                continue


            ### Left branch
            # if left branch is filled, change current node to this and continue the comparrison
            elif element < current_node.data and current_node.left_branch != None:
                if verbose == True:
                    print(element, ', moved left')
                    print('Current node:', current_node.data)
                    print('Left branch:', current_node.left_branch.data if current_node.left_branch != None else 'None')
                    print('Rigth branch:', current_node.right_branch.data if current_node.right_branch != None else 'None')
                    print()

                current_node = current_node.left_branch
                continue

            # if the element is less than the parent node, place it to the left
            elif element < current_node.data:
                current_node.left_branch = Node(
                    parent=current_node,
                    data=element,
                    original_index=index,
                    left_branch=None,
                    right_branch=None
                )
                inserted = True
                if verbose == True:
                    print('inserted', element, 'left')
                    print('Current node:', current_node.data)
                    print('Left branch:', current_node.left_branch.data if current_node.left_branch != None else 'None')
                    print('Rigth branch:', current_node.right_branch.data if current_node.right_branch != None else 'None')
                    print()
                    
                continue


    # returns the sorted binary tree
    print(binary_tree.data, binary_tree.left_branch, binary_tree.right_branch)
    return binary_tree


example_sorted_list = [12, 2, 3, 8, 29, 34, 47, 52, 61, 69, 83, 99]
example_unsorted_list = [12, 3, 99, 69, 47, 2, 52, 83, 61, 8, 29, 34]

wanted_element = 69


# binary search on sorted list
Binary_Search(
    element_list=example_sorted_list,
    desired_element=wanted_element
)



# sorting/inserting of unsorted list before performing binary search 
Binary_Tree_Insertion(
    unsorted_list=example_unsorted_list,
    verbose=True
)