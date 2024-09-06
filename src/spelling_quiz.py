import speech
from prompt_utils import generate_explanation
from utils import print_obfuscated


def dictation(word, words, content_generator, mod):
    while True:
        speech.say(word)
        answer = input("Type the word you heard (Enter-repeat, 1-definition, 2-hint): ")
        if answer == '':
            continue
        elif answer == '1':
            try:
                print("[thinking...]")
                print()
                e = generate_explanation(word)
                print_obfuscated(e, word, [])
                print()
            except:
                print("Error: cannot find the definition.")
        elif answer == '2':
            if len(word) > 1:
                print(word[0] + '_' * (len(word) - 1))
            else:
                print('_')
                print()
        else:
            break
    return answer.lower() == word.lower()
