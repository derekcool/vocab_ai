from utils import *
import reviews
from problems import multiple_choice_problem, fill_in_blanks_problem
from spelling_quiz import dictation
from prompt_utils import *
import myconfigs
import wordlist
import progress


def practice_menu():
    while True:
        if len(wordlist.words) == 1:
            print("1 word")
        else:
            print("{} words".format(len(wordlist.words)))
        print("------------------------")
        print("1: review")
        print("2: dictation")
        print("3: find the missing word in a sentence (MC)")
        print("4: guess the correct word from the definition (MC)")
        print("5: find the missing word in a sentence (Type)")
        print("6: guess the correct word from the definition (Type)")
        print("q: quit to previous menu")
        print()
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            reviews.review_quiz(wordlist.words)
        elif prog == '2':
            problem_loop(wordlist.words, dictation, None, None, True)
        elif prog == '3':
            problem_loop(wordlist.words, multiple_choice_problem, generate_example, None, True)
        elif prog == '4':
            problem_loop(wordlist.words, multiple_choice_problem, generate_explanation, "using 1 sentence", False)
        elif prog == '5':
            problem_loop(wordlist.words, fill_in_blanks_problem, generate_example, None, True)
        elif prog == '6':
            problem_loop(wordlist.words, fill_in_blanks_problem, generate_explanation, "using 1 sentence", False)


def problem_loop(words, problem_generator, content_generator, mod, option_show_explanation):
    random.shuffle(words)
    if myconfigs.configs["word_sort_rule"] == "progress":
        words.sort(key=sort_progress)
    num_correct = 0
    total = 0
    for word in words:
        total += 1
        print("[creating quiz {}/{} ...]".format(total, len(words)))
        print()
        progress.inc_progress_total(word)
        is_correct = problem_generator(word, words, content_generator, mod)
        if is_correct:
            print()
            print("\tCorrect!")
            num_correct += 1
            progress.inc_progress_correct(word)
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
            progress.save_progress()
            break
        print()
    print("Summary: total corrects = {}/{} ({:.1f}%)".format(num_correct, total, num_correct * 100 / total))
    print()
    input("Press 'Enter' to continue.")
