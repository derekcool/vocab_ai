import random
from utils import *
from review_words import review_words
from problems import multiple_choice_problem
from content_utils import generate_example, generate_explanation
import sys
import myconfigs


def problem_loop(words, problem_generator, content_generator, option_show_explanation):
    random.shuffle(words)
    num_correct = 0
    total = 0
    for word in words:
        total += 1
        print("[creating quiz {}/{} ...]".format(total, len(words)))
        print()
        is_correct = problem_generator(word, words, content_generator)
        if is_correct:
            print()
            print("\tCorrect!")
            num_correct += 1
        else:
            print("\tIncorrect. The answer is {}.".format(word))
        print()
        cmd = None
        while cmd is None:
            if option_show_explanation:
                cmd = input("Press 'Enter' the next quiz. 'e' to show definition. 'q' to quit")
            else:
                cmd = input("Press 'Enter' the next quiz. 'q' to quit")
            if cmd == 'e':
                try:
                    e = generate_explanation(word)
                    print()
                    print(e)
                except:
                    print("Error: AI cannot find any definition about this word.")
                print()
                cmd = None
            elif cmd == 'q':
                break
        if cmd == 'q':
            break
        print()
    print("Summary: total corrects = {}/{} ({:.1f}%)".format(num_correct, total, num_correct * 100 / total))
    print()
    input("Press 'Enter' to continue.")


def main_loop(words):
    while True:
        print("1: review words.")
        print("2: find the missing word in a sentence (MC)")
        print("3: guess the correct word from the definition (MC)")
        print("q: exit")
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            review_words(words)
        elif prog == '2':
            problem_loop(words, multiple_choice_problem, generate_example, True)
        elif prog == '3':
            problem_loop(words, multiple_choice_problem, generate_explanation, False)
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



