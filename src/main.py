import random
from utils import *
from reviews import review_words
from missing_word_quiz import missing_word_quiz
import sys


def main_loop(words):
    while True:
        print("1: review words.")
        print("2: missing word practice")
        print("q: exit")
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            review_words(words)
        elif prog == '2':
            missing_word_quiz(words)
        print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python src/main.py [words_file_path]")
    else:
        words = read_words(sys.argv[1])
        random.shuffle(words)
        # print(words)
        print("{} words read".format(len(words)))
        print()
        main_loop(words)



