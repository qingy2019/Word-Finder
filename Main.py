"""
Instructions:
1. Run this file to start the program.
2. Type in the first half of a word and hit enter.
3. The program will show possible completions of the word, if any.
"""

# 1. Searching through each of the words is a bit too slow, so I create a Trie class (Tries are data structures commonly used for these types of applications.)
# You can read more about Tries here: https://en.wikipedia.org/wiki/Trie

# 2. Read in data from words and store it in the trie.

# 3. Implement a function that takes in a prefix and returns a list of possible completions.

class TrieNode:
    def __init__(self):
        self.children = {} # The children of the node. Will store data in a dictionary like {'a': TrieNode, 'b': TrieNode, etc.}
        self.isEndOfWord = False
        self.possibleWords = [] # List of possible words that can be formed from the current node


# Main Code
wordsFile = open("words", "r") # Read in text from file
words = [] # List to store words

while True:
    nextLine = wordsFile.readline()
    if not nextLine: # Checks if nextLine is empty
        break
    words.append(nextLine[0:-1]) # Add word to list | Also uses [0:-1] to remove the newline character

root = TrieNode() # Create root node of Trie

for word in words:
    curr = root
    root.possibleWords.append(word)
    for charIdx in range(len(word)):
        character = word[charIdx]
        if character not in curr.children:
            curr.children[character] = TrieNode()
        curr = curr.children[character]
        curr.possibleWords.append(word)
        if charIdx == len(word) - 1:
            curr.isEndOfWord = True
            break

# Now the Trie is in place.

while True:
    startOfWord = input("Enter the first half of a word: ")
    curr = root
    found = True
    for char in startOfWord:
        if char not in curr.children:
            found = False
            break
        curr = curr.children[char]
    if not found:
        print("No words found.")
    else:
        print('----------------------')
        print("Possible completions:")
        for word in range(min(len(curr.possibleWords), 10)):
            print(curr.possibleWords[word])
        print('----------------------')