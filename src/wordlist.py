from utils import sort_progress


words = []
words_file = None


def load_words_from_file(filename):
    global words, words_file
    with open(filename) as f:
        words = []
        words_file = filename
        for line in f.readlines():
            if line.startswith("#"):
                continue
            word = line.strip('\n').lstrip().rstrip()
            if len(word) > 0:
                words.append(word)


def has_word(word):
    global words
    return word in words


def add_word(word):
    global words
    words.append(word)


def sort_words():
    global words
    words.sort(key=sort_progress)
