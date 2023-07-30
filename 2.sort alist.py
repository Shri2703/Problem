'''
Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.
'''

#solution

def sort_elements(elements, order):
    if order == 'asc':
        return sorted(elements)
    elif order == 'desc':
        return sorted(elements, reverse=True)
    elif order == 'none':
        return elements
    else:
        raise ValueError("Invalid sort order. Use 'asc', 'desc', or 'none'.")

# Example usage with numbers:
numbers_list = [5, 2, 8, 1, 9]
sorted_numbers_ascending = sort_elements(numbers_list, 'asc')
print("Sorted numbers in ascending order:", sorted_numbers_ascending)

# Example usage with strings:
strings_list = ["apple", "banana", "cherry", "orange"]
sorted_strings_descending = sort_elements(strings_list, 'desc')
print("Sorted strings in descending order:", sorted_strings_descending)

# Example usage with 'none' order:
original_list = [3, 1, 2]
sorted_none = sort_elements(original_list, 'none')
print("Original list:", sorted_none)
