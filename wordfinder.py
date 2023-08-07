"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("/student/words.txt") # Use relative pathname
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    
    def __init__(self, filename="words.txt") -> None:
        """Constructor method, filename should include path and filetype"""
        if not ".txt" in filename:
            filename += ".txt"
        
        self.filename = filename

        self.words_list = self.get_words(filename)

        self.words_count = len(self.words_list)

        print(f"{self.words_count} words read")
    
    def __str__(self) -> str:
        return f"I know {len(self.words_list)} words"
    
    def __repr__(self) -> str:
        return f"Wordfinder(filename={self.filename})"
    
    def get_words(self, filename) -> list:
        """Takes in a string and returns a list of the words in the associated file"""

        words_list = []

        file = open(filename, "r")

        for line in file:
            words_list.append(line.rstrip())

        file.close()

        return words_list
    
    def random(self) -> str:
        """Returns a random word from the read-in file"""

        index = randint(0, self.words_count - 1)
        return self.words_list[index]