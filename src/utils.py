import json
import requests
import myconfigs


def read_words(filename):
    words = []
    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            word = line.strip('\n').lstrip().rstrip()
            if len(word) > 0:
                words.append(word)
    return words


def sort_progress(word):
    return myconfigs.progress['correct'].get(word, 0)


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
