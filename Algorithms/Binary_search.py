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



example_sorted_list = [2, 3, 8, 29, 34, 47, 52, 61, 69, 83, 99]
example_unsorted_list = [3, 99, 69, 47, 2, 52, 83, 61, 8, 29, 34]

wanted_element = 69


# binary search on sorted list
Binary_Search(
    element_list=example_sorted_list,
    desired_element=wanted_element
)



# sorting/inserting of unsorted list before performing binary search 
