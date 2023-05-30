# - Implement a linked list data structure in your preferred programming language (Python or Java). 
#   Include methods for inserting a node at the beginning, inserting a node at the end, deleting a node, and searching for a node. 
# - Write a program that uses the linked list to store a list of integers and prints them in reverse order


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    

class Linked_List:
    def __init__(self, head_data=None):
        self.head = Node(data=head_data)
    
    def insert_start(self, node):
        # inserts node at front by:
        current_head = self.head
        node.next = current_head # selecting head to be new node's new next reference
        self.head = node # selecting head, swapping head to be new node
    
    def insert_end(self, node):
        # selects first (head) node and moves to end using "next" until this attribute equals "None"
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        # when "next" equals "None", were at the end. Inserts next node here
        current_node.next = node
    
    def display_links(self):
        current_node = self.head
        while current_node.next:
            print(' ', current_node.data)
            current_node = current_node.next
        
        print(' ', current_node.data)
    
    def search_links(self, node_data):
        # selects first (head) node, moves to end by swapping to next node using "next" until end
        current_node = self.head
        while current_node.next:
            print('checking', current_node.data)
            # checks if that node has the desired node value
            if current_node.data == node_data:
                print('Found node with value:')
                print('Node: ', current_node)
                print('Data: ', current_node.data)
                return
            
            # moves to next node
            current_node = current_node.next
        
        # checks if the last node has the desired node value
        if current_node.data == node_data:
            print('Found node with value:')
            print('Node: ', current_node)
            print('Data: ', current_node.data)
            return
        
        # if no match was found, it informs that it was not found
        else:
            print('No node with this value:', node_data)
            return


# For testing
test_LL = Linked_List(head_data=1)
test_Node1 = Node(data=2)
test_Node2 = Node(data=3)
test_Node3 = Node(data=4)
test_LL.insert_start(node=test_Node1)
test_LL.insert_end(node=test_Node2)
test_LL.insert_end(node=test_Node3)

test_LL.display_links()
test_LL.search_links(node_data=4)


# Program that stores elements in list and prints them in reverse order
insert_LL = Linked_List()
insertable_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(insertable_list)):
    # inserts into linked list in reverse order using the negative index (that selects from the end of the list)
    insert_element = insertable_list[-i -1]

    if i == 0:
        insert_LL.head.data = insert_element
    else:
        insert_LL.insert_end(node=Node(data=insert_element))


insert_LL.display_links()