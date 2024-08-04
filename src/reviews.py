import random
import speech
from content_utils import *
from utils import sort_progress


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
            cmd = input("1-definition. 2-example. 3-pronunciation. 4-next word. q-quit: ")
            if cmd == '1':
                print("[thinking...]")
                print()
                try:
                    exp = generate_explanation(word)
                    print(exp)
                except:
                    print("Error generating definition.")
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
            cmd = input("1-definition. 2-example. 3-next.")
            if cmd == '1':
                print("[thinking...]")
                print()
                try:
                    exp = generate_explanation(word)
                    print(exp)
                except:
                    print("Error generating definition.")
            elif cmd.startswith('2'):
                process_example_command(cmd, word)
            if cmd == '3' or cmd == 'q':
                break
            print()
        print()
