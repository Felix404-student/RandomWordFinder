"""Special Word Finder: finds random words from a dictionary, skipping blank lines and comments."""

from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """See parent class WordFinder. SpecialWordFinder ignores blank lines and comments in files."""

    def get_words(self, filename) -> list:
        """Takes in a string and returns a list of the words in the associated file"""

        words_list = []

        file = open(filename, "r")

        for line in file:
            next_line = line.rstrip()

            if not (next_line == '') and (not '#' in next_line):
                words_list.append(next_line)

        file.close()

        return words_list
    
