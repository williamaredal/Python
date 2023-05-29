# This search algorithm has a time complexity of O(n) due to: 
# - The algorithm iterates over all elements in the given list before it finds the element in it's worst case.
# - The data that is searched is not sorted in any manor

def Linear_Search(element_list, desired_element):
    for index, element in enumerate(element_list):
        if element == desired_element:
            print('Element found at index: ', index)
            return index

    print('Element not found in list')
    return -1


example_list = [16, 24, 11, 2, 59, 7, 69, 91, 5]
wanted_element = 69

Linear_Search(
    element_list=example_list,
    desired_element=wanted_element
)