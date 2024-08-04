import random
import speech
from prompt_utils import *
from utils import sort_progress


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
        while True:
            print()
            print("\t{}".format(word))
            print()
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
