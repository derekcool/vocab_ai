import random
import progress


def sort_progress(word):
    return progress.progress['correct'].get(word, 0)


def print_obfuscated(text, word, signatures):
    lines = text.split('\n')
    for line in lines:
        sigfound = False
        for sig in signatures:
            if line.startswith(sig):
                sigfound = True
                break
        if sigfound:
            continue
        if len(line) == 0:
            continue
        line = line.replace(word, "_____")
        word2 = word.capitalize()
        line = line.replace(word2, "_____")
        print(line, "\n")


def build_hint(word, indices):
    chars = []
    for i in range(len(word)):
        chars.append('_')
    for i in indices:
        chars[i] = word[i]
    return ''.join(chars)


def multiple_choice_candidates(word, words, n):
    candidates = random.sample(words, n)
    if word not in candidates:
        candidates.pop()
        candidates.insert(random.randint(0, len(candidates)), word)
    index = 0
    while index < len(candidates):
        if candidates[index] == word:
            break
        index += 1
    return candidates, index + 1
