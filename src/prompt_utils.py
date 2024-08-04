from query_utils import query
import myconfigs


def generate_explanation(word, style=None):
    level = myconfigs.configs["level"]
    if style is None:
        style = myconfigs.configs["definition_style"]
    if style == "":
        ep = query("What's the meaning of '{}' to a {}? Definition:".format(word, level))
    else:
        ep = query("What's the meaning of '{}' to a {}? Describe the definition {}. Definition:".format(word, level, style))
    if ep is None:
        raise Exception("AI didn't generate any explanation.")
    return ep


def generate_example(word, about=None):
    level = myconfigs.configs["level"]
    if about is not None:
        prompt = "Create a sentence about {}".format(about)
    else:
        prompt = "Create a sentence"
    e = query("{} using the word '{}' for a {}. sentence:".format(prompt, word, level))
    if e is None:
        raise Exception("AI didn't generate any examples.")
    return e


def generate_synonyms(word):
    level = myconfigs.configs["level"]
    e = query("What are the synonyms of '{}' to a {}?".format(word, level))
    if e is None:
        raise Exception("AI didn't find any synonyms.")
    return e


def explain_differences(word1, word2):
    level = myconfigs.configs["level"]
    e = query("Explain the difference between {} and {} to a {}. Explain in a short and concise way.".format(word1, word2, level))
    return e
