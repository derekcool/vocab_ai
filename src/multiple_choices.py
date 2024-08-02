import random


def multiple_choice_problem(words, question_generator):
    random.shuffle(words)
    num_correct = 0
    total = 0
    for word in words:
        total += 1
        candidates = random.sample(words, 4)
        if word not in candidates:
            candidates.pop()
            candidates.insert(random.randint(0, len(candidates)), word)
        print("[creating quiz {}/{} ...]".format(total, len(words)))
        print()
        e = question_generator(word)
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
                    is_correct = True
        except:
            if answer == word:
                is_correct = True
        if is_correct:
            print()
            print("\tCorrect!")
            num_correct += 1
        else:
            print("\tIncorrect. The answer is {}.".format(word))
        print()
        cmd = input("Press 'Enter' the next quiz. 'q' to quit")
        if cmd == 'q':
            break
    print()
    print("Summary: total corrects = {}/{} ({:.1f}%)".format(num_correct, total, num_correct * 100 / total))
    print()
    input("Press 'Enter' to continue.")




