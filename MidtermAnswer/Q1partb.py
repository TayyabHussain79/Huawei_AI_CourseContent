# def bracketsCheck(str):
#     if str.count("(") == str.count(")") and str.count("{") == str.count("}") and str.count("[") == str.count("]"):
#         return True
#     else:
#         return False

# result = bracketsCheck("[Hello(Tayyab) {Hope your are doing well}]")
# print(result)
# result = bracketsCheck("Hello(Tayyab) {Hope your are doing well}]")
# print(result)

def brackets_check(string):
    """
    Checks if all types of brackets in the string are balanced and properly nested.
    
    Parameters:
    string (str): The input string.

    Returns:
    bool: True if brackets are balanced and nested correctly, False otherwise.
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map:  # closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return not stack

# Example usage
print(brackets_check("[Hello(Tayyab) {Hope your are doing well}]"))  #True
print(brackets_check("Hello(Tayyab) {Hope your are doing well}]"))   #False
print(brackets_check("[(])"))       #False                                 
print(brackets_check("()[]{}"))   #True
