"""
TITLE: Password Generator
AUTHOR: Dylan Hartman
DATE: December 9, 2022

This script allows the user to generate a random password
    with the potential of changing what characters to add
    
This script has not error catching or has no speed advantage
"""

import random

def generatePassword(possible_characters, size_of_password):
    password = []
    character_list = list(possible_characters)
    for position in range(size_of_password):
        password.append(random.choice(character_list))
    return "".join(password)

characters = "abcdefghijklmnopqrstuvwxyz@#$%^&*()12345678"
size_of_password = input("Size of password: ")

result = generatePassword(characters, int(size_of_password))
print("Your password is: " + str(result))
