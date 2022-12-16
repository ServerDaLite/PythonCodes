'''
AUTHOR: Dylan Hartman
DATE: December 16, 2022
'''

class WordGame():
    
    def __init__(self, hidden_word: str):
        # Setting all characters in hidden word to uppercase
        # Setting the hidden word in to a list
        self.hidden_word = list(hidden_word.upper())
        
        # Getting the word count of all characters in list
        self.word_count = self.__getWordCount()
    
    # Function to count words a returns a dict
    def __getWordCount(self) -> dict():
        # Preseting a memory location
        memory = dict()
        
        # Looping through each character in hidden word
        for char in self.hidden_word:
            
            # If character is not in the memory
            if char not in memory:
                # Appending the character with value of 1
                memory[char] = 1
                continue
            
            # Adding one to character if in memory.
            memory[char] += 1
            
        # Returning the memory
        return memory
    
    # A function for user to guess a word
    def guessWord(self, guessed_word: str) -> list:
        
        # Check to see if guess word size is the same as hidden word size
        if len(guessed_word) != len(self.hidden_word):
            return f"Size not same"
        
        # Setting a memory for the results for user
        returned_word = list()
        
        # Setting all characters for memory to 0
        # Checking to see if any repeats are not there
        word_bank = {char: 0 for char in self.hidden_word}
        
        # Looping through each character with its index from the users input
        for idx, char in enumerate(guessed_word.upper()):
            if char == self.hidden_word[idx]:
                if word_bank[char] < self.word_count[char]:
                    returned_word.append(char)
                    word_bank[char] += 1
                    continue
                returned_word.append("*")
                continue
            
            elif char in self.hidden_word:
                if word_bank[char] < self.word_count[char]:
                    returned_word.append("+")
                    word_bank[char] += 1
                    continue
                returned_word.append("*")
                continue
            
            returned_word.append("*")
            
        return returned_word

if __name__ == "__main__":
    # Calling the 'WordGame()' class
    word_game = WordGame("Wooden")
    # Guesses a word for the hidden word
    result = word_game.guessWord("oodwen")
    # Displaying the results of the guessed to hidden
    print(result)

### END OF FILE ###
