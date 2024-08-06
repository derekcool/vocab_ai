import random
from utils import print_obfuscated, multiple_choice_candidates


def multiple_choice_problem(word, words, content_generator, mod):
    candidates, answer_index = multiple_choice_candidates(word, words, 4)
    e = content_generator(word, mod)
    print_obfuscated(e, word, ["Here is an example", "Here is a sentence using"])
    print()
    for i in range(len(candidates)):
        print("{}: {}".format(i+1, candidates[i]))
    print()
    answer = input("Select or type the correct word: ")
    try:
        i = int(answer)
        if i == answer_index:
            return True
    except:
        if answer == word:
            return True
    return False


def fill_in_blanks_problem(word, words, content_generator, mod):
    e = content_generator(word, mod)
    lines = e.split('\n')
    for line in lines:
        if line.startswith("Here is an example") or line.startswith("Here is a sentence using"):
            continue
        if len(line) == 0:
            continue
        if len(word) > 1:
            replacement = word[0] + '_' * (len(word) - 1)
        else:
            replacement = '_'
        line = line.replace(word, replacement)
        word2 = word.capitalize()
        line = line.replace(word2, replacement)
        print(line, "\n")
    print()
    answer = input("Type the missing word: ")
    return answer == word
