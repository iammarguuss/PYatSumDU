def find_letter_sets(text):

    at_least_twice = set()
    only_once = set()

    letter_count = {}
    for letter in text:
        if letter.isalpha(): 
            letter_count[letter] = letter_count.get(letter, 0) + 1

    for letter, count in letter_count.items():
        if count >= 2:
            at_least_twice.add(letter)
        else:
            only_once.add(letter)

    print("Letters appearing at least twice:", at_least_twice)
    print("Letters appearing only once:", only_once)

sample_text = "Example text with some letters appearing more than once and some only once"

find_letter_sets(sample_text)
