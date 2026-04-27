import re
import operator


def load_stop_words(stop_words_file_path: str) -> list:
    """Loads stop words from a file and return as a list of words.

    Keyword arguments:
    stop_words_file_path -- filepath of a file containing stop words
    """
    pass


def build_stop_word_regex(stop_words_file_path: str) -> re.Pattern:
    """Builds a regex expression to match any of the stop word.

    Keyword arguments:
    stop_words_file_path -- filepath of a file containing stop words
    """
    pass


class RAKE(object):
    def __init__(self, stop_words_file: str = 'resources/SmartStoplist.txt'):
        self.stop_words_file_path = stop_words_file
        self.stop_words_pattern = build_stop_word_regex(stop_words_file)

    def exec(self, text: str):
        pass

    def split_sentences(self, text: str) -> list:
        """Split text into sentences."""
        pass

    def generate_candidate_keywords(self, sentences: list) -> list:
        """
        Returns keyword phrases after removing stopwords from each sentence.
        """
        pass

    def is_number(self, s):
        pass

    def separate_words(self, text: str, word_min_size: int = 0) -> list:
        """
        Return a list of all words of length greater than specified min size.

        Keyword arguments:
        text -- the text that is to be split into words
        word_min_size -- the min. no. of characters a word must have (def: 0)
        """
        pass

    def calculate_word_scores(self, phrases: list) -> dict:
        """Calculates the word score for all the words in the phrases."""
        pass

    def generate_candidate_keyword_scores(self, phrases: list,
                                          word_score: dict) -> dict:
        """Returns the dict. of candidate keywords with scores."""
        pass
