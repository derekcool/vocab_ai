from word_list_menu import word_list_loop
from practice_menu import practice_menu
from explore_menu import explore_menu
import sys
import myconfigs
import speech
import wordlist


def main_loop(words):
    while True:
        if len(words) != 1:
            print("{} words".format(len(words)))
        else:
            print("1 word")
        print("----------------------")
        print("1: practice")
        print("2: explore")
        print("3: word list")
        print("q: exit")
        print()
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            practice_menu()
        elif prog == '2':
            explore_menu()
        elif prog == '13':
            word_list_loop()

        print()


if __name__ == '__main__':
    print("Vocab AI: seting up...")
    myconfigs.load_configs("configs.ini")
    myconfigs.load_configs("myconfigs.ini")
    if len(myconfigs.configs) == 0:
        print("Cannot find any configs. Load default configs.")
        myconfigs.load_default_configs()
    else:
        print("config loaded")
    for k, v in myconfigs.configs.items():
        if k == 'api_key':
            continue
        print("\t{} = {}".format(k, v))

    myconfigs.load_progress()
    speech.set_rate(myconfigs.configs["speech_rate"])

    print()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print("loading words from '{}'".format(filename))
        wordlist.load_words_from_file(filename)
        print("{} words read".format(len(wordlist.words)))
        print()

    print("------------------ Tip ----------------")
    print("[m] means you change the response from AI by appending context to the command selection.")
    print("Examples:")
    print("1-definition[m]: 1 using 1 sentence less than 8 words => generating definition using 1 sentence less than 8 words.")
    print("2-example[m]: 2 science => generating a example about science")
    print("---------------------------------------")

    main_loop(wordlist.words)
    myconfigs.save_progress()



