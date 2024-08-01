# Vocab AI
Practice vocabulary in several ways with the help of AI.

The default program uses Ollama API running locally.

But it can be easily modified to use other LLM, either online or locally. Check the query method in utils.py

Games includes
- review words with AI generated explanation and examples
- sentence with missing word quiz (multiple choice)

## How to use
1. run ollama, replace model name if necessary.
```commandline
ollama run llama3.1
```
2. modify configs.py to set the correct model name, level, etc.
3. run the main.py with the word filename
```
# Example
python src/main.py words/sample.txt
```

## Notes
You can put your own word files in mywords folder. It'll be git ignored.