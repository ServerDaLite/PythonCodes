"""
TITLE: Affine Cypher
AUTHOR: Dylan Hartman
DATE: December 9, 2022

This is a simple script that uses the Affine Cyher algorithm.
"""

# A list of the entire alphabet
alphebet = "abcdefghijklmnopqrstuvwxyz"

# Affine Cypher function
def affineCypher(slope, y_intercept, string):
    # Creating an empty list for the numbers
    numbers = list()
    
    # Lowering all characters within the string
    # Looping through each character of the string
    for character in string.lower():
        # Using the equation with the slope and y_intercept
        # Modulating the result of equation by 26
        # Appending the result to the 'numbers' list
        numbers.append(slope * alphebet.index(character) + y_intercept) % 26)
    
    # Creating a list for the results
    results = []
    
    # Looping through each number from 'numbers' list
    for number in numbers:
        # Finding the character from number
        results.append(alphebet[number])
        
    # Combining the 'results' variable
    # returning the combined 'results' variable
    return "".join(results)

### SETTINGS ###
a = input("Enter a slope value: ")
b = input("Enter a Y intercept value: ")
string = input("Enter a string to cypher: ")

# Using function 'affineCypher()' and inputting variables
results = affineCypher(a, b, string)

# Printing the results
print(results)
        
        
