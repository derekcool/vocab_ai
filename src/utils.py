import json
import requests
import myconfigs


def query(prompt):
    url = "http://{}:{}/api/generate".format(myconfigs.configs["host"], myconfigs.configs["port"])
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": myconfigs.configs["model"],
        "prompt": prompt,
        "stream": False
    }
    if myconfigs.configs["debug"]:
        print("sending prompt:", prompt)
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        restext = response.text
        data = json.loads(restext)
        return data["response"]
    else:
        print("Error:", response.status_code, response.text)
        return None


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
