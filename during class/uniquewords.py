import re

def unique_words(filename):
    unique_words_set = set()
    
    with open(filename, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            unique_words_set.update(words)
    return unique_words_set

filename = 'first\words.txt'
unique_words_set = unique_words(filename)
print(f"Number of unique words: {len(unique_words_set)}")