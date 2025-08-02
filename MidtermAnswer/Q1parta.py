# def EvenListerReturn(list):
#     evenList = [i**2 for i in list if i%2==0]
#     return evenList

# evenList = EvenListerReturn([1,4,6,2,3,7])
# print(evenList)

def get_squared_evens(input_list):
    """
    Returns a list containing the squares of even numbers from the input list.
    
    Parameters:
    input_list (list): A list of integers.

    Returns:
    list: A list of squared even integers.
    """
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    
    for item in input_list:
        if not isinstance(item, int):
            raise ValueError("All elements in the list must be integers.")
    
    return [i**2 for i in input_list if i % 2 == 0]

# Example usage
even_squares = get_squared_evens([1, 4, 6, 2, 3, 7])
print(even_squares)
