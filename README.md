# RandomWordFinder
Python utility for retrieving words from text files

Word Finder: finds random words from a dictionary.
Special Word Finder skips blank lines and comments.
    
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


