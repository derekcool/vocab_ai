import reviews
from prompt_utils import *
import myconfigs
import wordlist
from synonyms import synonyms


def explore_menu():
    while True:
        if len(wordlist.words) == 1:
            print("1 word")
        else:
            print("{} words".format(len(wordlist.words)))
        print("------------------------")
        print("1: dictionary")
        print("2: synonym")
        print("3: differences")
        print("4: make a sentence")
        print("q: quit to previous menu")
        print()
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        elif prog == '1':
            reviews.dictionary()
        elif prog == '2':
            synonyms()
        elif prog == '3':
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            print("[looking for differences between {} and {}...]".format(word1, word2))
            print()
            e = explain_differences(word1, word2)
            print(e)
            print()
            input("Enter to quit.")
        elif prog == '4':
            while True:
                word = input("Which word would you use? (l-list words, q-quit): ")
                if word == 'l':
                    print(wordlist.words)
                    print()
                    continue
                elif word == 'q':
                    break
                print()
                cmd = None
                while cmd != 'q':
                    print("Make a sentence with '{}'.".format(word))
                    sentence = input()
                    print()
                    print("[Analyzing...]")
                    level = myconfigs.configs["level"]
                    analysis = query(
                        "Analyze the following sentence made with the word '{}'. Comment on what user did right, what to improve. Do not provide edited version for the user. The comment should target a {}. sentence: {}; comment:".format(
                            word, level, sentence))
                    print(analysis)
                    print()
                    cmd = 'i'
                    while cmd == 'i':
                        cmd = input("m-make another sentence. i-improve the sentence. Enter-try another word")
                        if cmd == 'm':
                            continue
                        elif cmd == 'i':
                            print("[improving...]")
                            improvement = query(
                                "Improve the following sentence for a {}. The new sentence must include the word '{}'. sentence: {}; improvement:".format(
                                    level, word, sentence))
                            print()
                            print(improvement)
                            print()
                    if cmd == '':
                        break
