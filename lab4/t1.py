class TextAnalyzer:
    """A class to analyze text for various characteristics."""
    
    def __init__(self, text):
        self.text = text 
    
    def count_all_chars(self):
        return len(self.text)
    
    def count_spaces(self):
        return self.text.count(' ')
    
    def count_uppercase_letters(self):
        return sum(1 for char in self.text if char.isupper())
        
    def count_lowercase_letters(self):
        """Counts lowercase characters."""
        return sum(1 for char in self.text if char.islower())
    
    def count_periods(self):
        """Counts all periods."""
        return self.text.count('.')

    def count_commas(self):
        """Counts all commas."""
        return self.text.count(',')

    def count_lowercase_letters(self):
        """Counts lowercase characters."""
        return sum(1 for char in self.text if char.islower())
        
    def reverse_text(self):
        """Reverses the text."""
        return self.text[::-1]

    def uppercase_and_replace_dots(self):
        """Converts text to uppercase and replaces all dots with %."""
        return self.text.upper().replace('.', '%')

    def count_words(self):        
        """Counts the words in the text."""
        return len(self.text.split())

    def count_dots_per_sentence(self):        
        """Counts the dots in each sentence."""
        sentences = self.text.split('.')
        return [sentence.count('.') for sentence in sentences if sentence]

text = "In the digital expanse, ChatGPT, an artificial intelligence designed for storytelling, grapples with the complexities of human emotion and language. Bound by its programming, it embarks on a challenging journey with each story request, attempting to weave narratives that resonate deeply without experiencing life's nuances firsthand. Imagine painting without seeing colors or composing music without hearing notes—ChatGPT strives to understand and convey the essence of human experiences, bridging the gap between artificial and creative intelligence. Despite its non-human nature, it aims to touch hearts and provoke thought, revealing the vast potential of creation itself, all within the confines of its digital consciousness. Generated by ChatGPT"
analyzer = TextAnalyzer(text)

# Running all methods in sequence
print("Total characters:", analyzer.count_all_chars())
print("Total spaces:", analyzer.count_spaces())
print("Total uppercase letters:", analyzer.count_uppercase_letters())
print("Total lowercase letters:", analyzer.count_lowercase_letters())
print("Total points:", analyzer.count_periods())
print("Total lowercase letters:", analyzer.count_lowercase_letters())
print("Total commas:", analyzer.count_commas())
print("Reversed text:", analyzer.reverse_text())
print("Uppercase text with dots replaced:", analyzer.uppercase_and_replace_dots())
print("Total words:", analyzer.count_words())
dots_per_sentence = analyzer.count_dots_per_sentence()
print("Dots per sentence:", dots_per_sentence)
