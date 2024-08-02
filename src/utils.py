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
