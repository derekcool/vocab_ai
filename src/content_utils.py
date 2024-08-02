from utils import query
import myconfigs


def generate_explanation(word):
    level = myconfigs.configs["level"]
    ep = query("Explain the meaning of '{}' to a {} using 1 concise sentence? Definition:".format(word, level))
    if ep is None:
        raise Exception("AI didn't generate any explanation.")
    return ep


def generate_example(word):
    level = myconfigs.configs["level"]
    e = query("Create a sentence using the word '{}' for a {}. sentence:".format(word, level))
    if e is None:
        raise Exception("AI didn't generate any examples.")
    return e
