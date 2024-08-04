# Vocab AI
Practice vocabulary in several ways with the help of AI.

The default program uses Ollama API running locally.

But it can be easily modified to use other LLM, either online or locally. Check the query method in utils.py

Games includes
- review words with AI generated explanation and examples
- sentence with missing word quiz (multiple choice)
- guess the correct word from the definition.

Question format includes
- multiple choice
- fill-in the blank

## Setup AI
### Ollama
run ollama3.1, replace model name if necessary.
```commandline
ollama run llama3.1
```

## How to use
1. run setup.sh, it will generate myconfigs.ini file where you can customize settings. It will also create a mywords dir where you can place your own word list files.
```
./setup.sh
```
2. run the main.py with the word filename
```
# Example
python src/main.py words/sample.txt

# or without word list
python src/main.py
```

## Customization
### User Word Files
You can create your own word file and put them in the mywords folder. This folder is not tracked by git.

The file format is one word per line.
```
word1
word2
word3
...

```

You can add comment to the file using the format
```
# comment here
```

### myconfigs.ini
You can overwrite the default configs.ini values by adding key=value pair in the myconfigs.ini. 

This file is not tracked by git. Some of the common configs you might customize are

#### level
This config describes the target user, which will allow AI to generate explanation, quiz or examples targeting those target users.

Example: following are all legitimate values. AI is flexible.
- level = grade 4 student
- level = university student
- level = professional

#### model
Change this to match the model name you run using ollama.
