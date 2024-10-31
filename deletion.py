def delete_element_at_position(lst, position):
    """
    Delete an element from a specific position in a list.

    Parameters:
    lst (list): The list from which to delete the element.
    position (int): The position of the element to delete.

    Returns:
    list: The list after deletion.
    """
    if position < 0 or position >= len(lst):
        raise IndexError("Position out of range")
    del lst[position]
    return lst

# Example usage
my_list = [1, 2, 3, 4, 5]
position_to_delete = 2  # This will delete the element at index 2 (which is 3)
print("Original list:", my_list)
updated_list = delete_element_at_position(my_list, position_to_delete)
print("Updated list:", updated_list)
