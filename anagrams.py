from collections import Counter
from collections.abc import Callable

def list_iter(words):
    """
    generator function to iterate over list of words
    :param words (str): space separted list of words
    :return: word (str) : individual word
    """
    for word in words.split():
        yield word

def process(reference: str) -> Callable[str]:
    """
    preprocess list of words which may contain anagrams and return closure

    :param reference: (str) : the list of newline separted input words
    :return: find_anagrams (callable) : closure to find anagram
    """

    words = reference.replace('\n', ' ')
    words_iter = list_iter(words)

    def find_anagrams(word: str) -> str:
        """
        find the anagram of word using a Counter which compares the frequency of characters
        in the word and each word in the list
        :param word (str) : the word to find anagrans of
        :return: (str) : newline separated list of words
        """
        anagrams = []
        for item in words_iter:
            if item != word and Counter(item) == Counter(word):
                anagrams.append(item)
        return "\n".join(anagrams)

    return find_anagrams

def main() -> None:
    """
    determine anagrams of a word contained in a string of newline separated words

    :param None
    :return: None
    """

    data = """
            starlet
            startle
            reduces
            rescued
            realist
            recused
            saltier
            retails
            secured
            """

    find_anagrams = process(reference=data)
    results = find_anagrams(word="rescued")
    print(results)


if __name__ == '__main__':
    """
    entry point of module, tested using Python 3.9
    run module using python -m anagrams
    """
    main()