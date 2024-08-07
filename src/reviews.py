import random
import numpy as np
import myconfigs
import progress
import speech
from prompt_utils import *
from utils import sort_progress, build_hint, multiple_choice_candidates


def process_definition_command(cmd, word):
    tokens = cmd.split(' ', maxsplit=1)
    if len(tokens) > 1:
        style = tokens[1]
    else:
        style = myconfigs.configs["definition_style"]
    print("[looking ({})...".format(style))
    print()
    try:
        exp = generate_explanation(word, style)
        print(exp)
    except:
        print("Error generating definition.")


def process_example_command(cmd, word):
    tokens = cmd.split(' ', maxsplit=1)
    if len(tokens) > 1:
        about = tokens[1]
        print("[generating example about {}...]".format(about))
    else:
        about = None
        print("[generating example...]")
    print()
    try:
        exp = generate_example(word, about)
        print(exp)
    except:
        print("Error generating definition.")


def review_words(words):
    random.shuffle(words)
    words.sort(key=sort_progress)
    total = 0
    for word in words:
        total += 1
        print("[{}/{}]".format(total, len(words)))
        print()
        print("\t{}".format(word))
        print()
        while True:
            cmd = input("1-definition[m]. 2-example[m]. 3-pronunciation. 4-next word. q-quit: ")
            if cmd.startswith('1'):
                process_definition_command(cmd, word)
            elif cmd.startswith('2'):
                process_example_command(cmd, word)
            elif cmd == '3':
                speech.say(word)
            elif cmd == '4' or cmd == 'q':
                break
            print()
        print()
        if cmd == 'Q' or cmd == 'q':
            break


def dictionary():
    word = ''
    while word != 'q':
        word = input("Enter a word (q to quit): ")
        word = word.lstrip().rstrip()
        if word == 'q':
            break
        while True:
            print()
            print(word)
            print()
            cmd = input("1-definition[m]. 2-example[m]. 3-pronunciation. 4-next.")
            if cmd.startswith('1'):
                process_definition_command(cmd, word)
            elif cmd.startswith('2'):
                process_example_command(cmd, word)
            elif cmd == '3':
                speech.say(word)
            elif cmd == '4' or cmd == 'q':
                break
            print()
        print()


def review_quiz(words):
    random.shuffle(words)
    words.sort(key=sort_progress)
    total = 0
    num_correct = 0
    for word in words:
        total += 1
        print("[{}/{}]".format(total, len(words)))
        # dictation
        hint_used = False
        # hint_indices = np.random.permutation(len(word))
        hint_indices = np.arange(len(word))
        max_hint_index = len(word) - 1
        hint_index = min(1, max_hint_index)
        while True:
            speech.say(word)
            answer = input("Type the word you heard (Enter-repeat. 1-hint): ")
            if answer == '':
                continue
            elif answer == '1':
                hint_used = True
                hint = build_hint(word, hint_indices[:hint_index])
                if hint_index < max_hint_index:
                    hint_index += 1
                print(hint)
                print()
            else:
                progress.inc_progress_total(word)
                if answer == word:
                    num_correct += 1
                    if not hint_used:
                        progress.inc_progress_correct(word)
                    print()
                    print("\tCorrect!")
                    print()
                else:
                    print()
                    print("\tIncorrect. The answer is {}".format(word))
                    print()
                break
        print("[Select the correct definition for '{}']".format(word))
        total += 1
        print()
        candidates, answer_index = multiple_choice_candidates(word, words, 3)
        i = 1
        for c in candidates:
            _d = short_definition(c)
            # _d = _d.replace(word, "_____")
            # word2 = word.capitalize()
            # _d = _d.replace(word2, "_____")
            print("{}: {}".format(i, _d))
            i += 1
        print()
        while True:
            answer = input("Which definition is correct?: ".format(word))
            try:
                i = int(answer)
            except:
                continue
            progress.inc_progress_total(word)
            if i == answer_index:
                progress.inc_progress_correct(word)
                num_correct += 1
                print()
                print("\tCorrect!")
                print()
            else:
                print()
                print("\tIncorrect! The correct answer is {}.".format(answer_index))
                print()
            break
        cmd = input("Enter for the next word. q-quit")
        if cmd == 'q':
            progress.save_progress()
            break
    print()
    print("correct / total = {}/{} = {:.1f}%".format(num_correct, total, num_correct * 100 / total))
    print()
    input("Enter to exit reviews")


