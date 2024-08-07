import wordlist
import progress
import os
from reviews import review_words


def word_list_loop():
    while True:
        if wordlist.words_file is not None:
            print("{}: {} words".format(wordlist.words_file, len(wordlist.words)))
            print("-------------------------")
            print("1: load word list")
            print("2: create word list")
            print("3: add word")
            print("4: review words")
            print("5: show progress")
            print("q: quit to previous menu")
            print()
            prog = input("select the program number: ")
            if prog == 'q':
                break
            if prog == '1':
                menu_load_word()
            elif prog == '2':
                menu_create_word_list()
            elif prog == '3':
                menu_add_word()
            elif prog == '4':
                review_words(wordlist.words)
            elif prog == '5':
                wordlist.sort_words()
                print("n_correct : word")
                print("--------------------")
                for word in wordlist.words:
                    c = progress.get_progress_correct(word)
                    print("{}: {}".format(c, word))
                print()
                input("Enter to continue")


def menu_load_word():
    path = input("enter the file path: ")
    if os.path.exists(path):
        wordlist.load_words_from_file(path)
        print("{} words loaded".format(len(wordlist.words)))
    else:
        print("Sorry this file does not exist.")
    print()
    input("Enter to continue")


def menu_create_word_list():
    while True:
        path = input("enter the file path: ")
        if os.path.exists(path):
            print("Error: the file already exists.")
            print()
        else:
            break
    with open(path, 'a') as f:
        wordlist.load_words_from_file(path)
        print("Create a new word list file: {}".format(wordlist.words_file))
        print()
        input("Enter to continue")


def menu_add_word():
    if wordlist.words_file is None:
        print("Error: you must first create / open a word list file.")
        return
    new_words = []
    while True:
        word = input("Enter a new word (q to quit): ")
        word = word.lstrip().rstrip()
        if wordlist.has_word(word):
            print("Error: this word already exist.")
            continue
        if word == 'q':
            break
        wordlist.add_word(word)
        new_words.append(word)
    if len(new_words) > 0:
        with open(wordlist.words_file, 'a') as f:
            for word in new_words:
                f.write("{}\n".format(word))
            print("{} words added to the file {}.".format(len(new_words), wordlist.words_file))
            print()
            input("Enter to continue")
