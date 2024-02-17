word1 = "Wordone"
word2 = "Superwordy"

unique_letters = ''.join(set(word1) ^ set(word2))

print("Unique letters found in only one of the words:", unique_letters)