import random
from explanation import generate_example, generate_explanation


def missing_word_quiz(words):
    random.shuffle(words)
    for word in words:
        candidates = random.sample(words, 4)
        if word not in candidates:
            candidates.pop()
            candidates.insert(random.randint(0, len(candidates)), word)
        print("[creating quiz...]")
        print()
        e = generate_example(word)
        lines = e.split('\n')
        for line in lines:
            if line.startswith("Here is an example"):
                continue
            if line.startswith("Here is a sentence using the word"):
                continue
            if len(line) == 0:
                continue
            line = line.replace(word, "_____")
            print(line, "\n")
        print()
        for i in range(len(candidates)):
            print("{}: {}".format(i+1, candidates[i]))
        print()
        while True:
            answer = input("select the correct word to fill the blank:")
            try:
                i = int(answer) - 1
                if 0 <= i < len(candidates):
                    if candidates[i] == word:
                        print("correct")
                    else:
                        print("The correct answer is {}.".format(word))
                    break
            except:
                print("enter the number next to the word.")
        print()
        cmd = input("Press 'e' for explanation. 'q' to quit. Other for the next quiz.")
        if cmd == 'e':
            try:
                print("[explanation: ...]")
                explanation = generate_explanation(word)
                print()
                print(explanation)
                input("Press anything for the next quiz.")
            except:
                print("Error: cannot find the explanation.")
        elif cmd == 'q':
            break



