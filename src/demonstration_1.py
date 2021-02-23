"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""


def to_lower_case(string):
    # Create an empty string / list to add our output
    output = ""
    for char in string:
        # Convert each char to num
        encoded_num = ord(char)
        # if num is between 65 and 90 add 32
        if 65 <= encoded_num <= 90:
            encoded_num += 32
        # convert back
        output += chr(encoded_num)
    return output

print(to_lower_case("LambdaSchool"))
