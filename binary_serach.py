#binary_serach.py

def binary_search(input_array, value):
    """Your code goes here."""
    if len(input_array) % 2 == 0:
        middle_element = input_array[len(input_array)/2 - 1]
    else:
        middle_element = input_array[len(input_array)/2]
        
    check_element = None
    index_val = None
    
    while check_element!= value or array_index :
        if value == middle_element:
            print('Search Element found at index {}'.format(input_array.index(value)))
            return 1
            break
        elif value > middle_element :
            new_array = input_array[middle_element:]
        elif value < middle_element:
            new_array = input_array[:middle_element]
        middle_element = new_array[len(new_array)/2]
    
    print('Value doesn\'t exist in the given list')
    return -1


