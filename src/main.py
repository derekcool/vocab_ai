import random
from utils import *
from review_words import review_words
from multiple_choices import multiple_choice_problem
from generators import generate_example, generate_explanation
import sys
import myconfigs


def main_loop(words):
    while True:
        print("1: review words.")
        print("2: missing word practice")
        print("3: correct word practice")
        print("q: exit")
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            review_words(words)
        elif prog == '2':
            multiple_choice_problem(words, generate_example)
            # missing_word_quiz(words)
        elif prog == '3':
            multiple_choice_problem(words, generate_explanation)
            # correct_word_quiz(words)
        print()


if __name__ == '__main__':
    myconfigs.load_configs("configs.ini")
    myconfigs.load_configs("user_configs.ini")
    if len(myconfigs.configs) == 0:
        print("Cannot find any configs. Load default configs.")
        myconfigs.load_default_configs()
    else:
        print("config loaded")
    for k, v in myconfigs.configs.items():
        print("\t{} = {}".format(k, v))
    print()
    if len(sys.argv) != 2:
        print("Usage: python src/main.py [words_file_path]")
    else:
        filename = sys.argv[1]
        print("loading words from '{}'".format(filename))
        words = read_words(filename)
        random.shuffle(words)
        print("{} words read".format(len(words)))
        print()
        main_loop(words)



