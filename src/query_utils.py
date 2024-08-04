import requests
import json

import myconfigs


def juhe_query(prompt):
    message = [
        {
            'role': "system",
            'content': "You are a English teacher"
        },
        {
            'role': 'user',
            'content': prompt,
        },
    ]
    api_key = myconfigs.configs["api_key"]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'model': 'gpt-4-1106-preview',
        'messages': message,
    }
    response = requests.post('https://api.juheai.top/v1/chat/completions', headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        json = response.json()
        content = json['choices'][0]['message']['content']
        return content
    return None


def ollama_query(prompt):
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


def query(prompt):
    ai = myconfigs.configs["ai"]
    if ai == 'ollama':
        return ollama_query(prompt)
    elif ai == 'danke':
        return juhe_query(prompt)
    raise("Error: AI '{}' is not supported yet.".format(ai))
