import random
from explanation import generate_explanation, generate_example


def review_words(words):
    random.shuffle(words)
    for word in words:
        print(word)
        print()
        while True:
            cmd = input("1-explanation. 2-example. 3-next word. q-quit")
            if cmd == '1':
                print("thinking...")
                print()
                try:
                    exp = generate_explanation(word)
                    print(exp)
                except:
                    print("Error generating explanation.")
            elif cmd == '2':
                print("thinking...")
                print()
                try:
                    exp = generate_example(word)
                    print(exp)
                except:
                    print("Error generating explanation.")
            if cmd == '3' or cmd == 'q':
                break
        print()
        if cmd == 'Q' or cmd == 'q':
            break
