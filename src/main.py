import random
from utils import *
from review_words import review_words
from problems import multiple_choice_problem, fill_in_blanks_problem
from content_utils import generate_example, generate_explanation
import sys
import os.path
import myconfigs


def problem_loop(words, problem_generator, content_generator, option_show_explanation):
    random.shuffle(words)
    num_correct = 0
    total = 0
    for word in words:
        total += 1
        print("[creating quiz {}/{} ...]".format(total, len(words)))
        print()
        myconfigs.progress["total"][word] = myconfigs.progress["total"].get(word, 0) + 1
        is_correct = problem_generator(word, words, content_generator)
        if is_correct:
            print()
            print("\tCorrect!")
            num_correct += 1
            myconfigs.progress["correct"][word] = myconfigs.progress["correct"].get(word, 0) + 1
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


def create_edit_word_list():
    path = input("enter the file path: ")
    if os.path.exists(path):
        _words = read_words(path)
    else:
        _words = []
    if len(_words) > 0:
        print("loaded {} words:".format(len(_words)))
        print(_words)
    print()
    new_words = []
    while(True):
        word = input("Enter a new word (q to quit): ")
        word = word.lstrip().rstrip()
        if word in _words:
            print("Error: this word already exist.")
            continue
        if word == 'q':
            break
        _words.append(word)
        new_words.append(word)
    if len(new_words) > 0:
        with open(path, 'a') as f:
            for word in new_words:
                f.write("{}\n".format(word))
            print("{} words added to the file {}.".format(len(new_words), path))
    cmd = input("replace current word list? [y/n]")
    if cmd == 'y':
        return _words
    return None


def main_loop(words):
    while True:
        if len(words) != 1:
            print("{} words".format(len(words)))
        else:
            print("1 word")
        print("----------------------")
        print("1: review words.")
        print("2: find the missing word in a sentence (MC)")
        print("3: guess the correct word from the definition (MC)")
        print("4: find the missing word in a sentence (Type)")
        print("5: guess the correct word from the definition (Type)")
        print("6: create/edit word list")
        print("7: load word list")
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
        elif prog == '4':
            problem_loop(words, fill_in_blanks_problem, generate_example, True)
        elif prog == '5':
            problem_loop(words, fill_in_blanks_problem, generate_explanation, False)
        elif prog == '6':
            new_words = create_edit_word_list()
            if new_words is not None:
                words = new_words
        elif prog == '7':
            path = input("enter the file path: ")
            if os.path.exists(path):
                words = read_words(path)
                print("{} words loaded".format(len(words)))
            else:
                print("Sorry this file does not exist.")
                print()
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

    myconfigs.load_progress()

    print()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print("loading words from '{}'".format(filename))
        words = read_words(filename)
        random.shuffle(words)
        print("{} words read".format(len(words)))
        print()
    else:
        words = []
    main_loop(words)
    myconfigs.save_progress()



