import random
from explanation import generate_example, generate_explanation


def correct_word_quiz(words):
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
        e = generate_explanation(word)
        lines = e.split('\n')
        for line in lines:
            if line.startswith("Here is an example"):
                continue
            if line.startswith("Here is a sentence using the word"):
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
        while True:
            answer = input("Select the correct word that match the definition: ")
            try:
                i = int(answer) - 1
                if 0 <= i < len(candidates):
                    if candidates[i] == word:
                        print("correct")
                        num_correct += 1
                    else:
                        print("The correct answer is {}.".format(word))
                    break
            except:
                print("enter the number next to the word.")
        print()
        cmd = input("Press 'Enter' the next quiz. 'q' to quit")
        if cmd == 'q':
            break
    print()
    print("Summary: total corrects = {}/{} ({:.1f}%)".format(num_correct, total, num_correct * 100 / total))
    print()
    input("Press 'Enter' to continue.")



