from utils import query
import configs as configs


def generate_explanation(word):
    ep = query("Explain the meaning of '{}' to a {}? Answer should be short.".format(word, configs.level))
    if ep is None:
        raise Exception("AI didn't generate any explanation.")
    return ep


def generate_example(word):
    e = query("Create a sentence using the word '{}' for a {}.".format(word, configs.level))
    if e is None:
        raise Exception("AI didn't generate any examples.")
    return e