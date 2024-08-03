import speech
from content_utils import generate_explanation
from utils import print_obfuscated


def dictation(word, words, content_generator):
    while True:
        speech.say(word)
        answer = input("Type the word you heard (Enter-repeat, 1-definition): ")
        if answer == '':
            continue
        elif answer == '1':
            try:
                e = generate_explanation(word)
                print_obfuscated(e, word)
                print()
            except:
                print("Error: cannot find the definition.")
        else:
            break
    return answer == word
