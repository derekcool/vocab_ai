from prompt_utils import generate_synonyms


def synonyms():
    word = ''
    while word != 'q':
        word = input("Enter a word (q to quit): ")
        word = word.lstrip().rstrip()
        if word == 'q':
            break
        print("[thinking...]")
        print()
        e = generate_synonyms(word)
        print(e)
        print()
