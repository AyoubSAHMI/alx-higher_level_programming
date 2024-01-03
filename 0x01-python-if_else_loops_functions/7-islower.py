#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is within the lowercase range
    return 97 <= ord(c) <= 122

# Example usage:
print(islower('a'))  # Output: True
print(islower('Z'))  # Output: False
print(islower('7'))  # Output: False
