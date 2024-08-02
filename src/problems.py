import random


def multiple_choice_problem(word, words, content_generator):
    candidates = random.sample(words, 4)
    if word not in candidates:
        candidates.pop()
        candidates.insert(random.randint(0, len(candidates)), word)
    e = content_generator(word)
    lines = e.split('\n')
    for line in lines:
        if line.startswith("Here is an example") or line.startswith("Here is a sentence using"):
            continue
        if len(line) == 0:
            continue
        line = line.replace(word, "_____")
        word2 = word.capitalize()
        line = line.replace(word2, "_____")
        print(line, "\n")
    print()
    for i in range(len(candidates)):
        print("{}: {}".format(i+1, candidates[i]))
    print()
    answer = input("Select or type the correct word: ")
    is_correct = False
    try:
        i = int(answer) - 1
        if 0 <= i < len(candidates):
            if candidates[i] == word:
                return True
    except:
        if answer == word:
            return True
    return False


def fill_in_blanks_problem(word, words, content_generator):
    e = content_generator(word)
    lines = e.split('\n')
    for line in lines:
        if line.startswith("Here is an example") or line.startswith("Here is a sentence using"):
            continue
        if len(line) == 0:
            continue
        line = line.replace(word, "_____")
        word2 = word.capitalize()
        line = line.replace(word2, "_____")
        print(line, "\n")
    print()
    answer = input("Type the missing word: ")
    return answer == word
