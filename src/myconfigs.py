import configparser
import pickle
import os.path


configs = {}
progress = {}


def load_configs(filename):
    global configs
    config = configparser.ConfigParser()
    config.read(filename)
    for section in config.sections():
        options = config.options(section)
        for opt in options:
            value = config.get(section, opt)
            if opt == "debug":
                if value == "yes":
                    configs[opt] = True
                else:
                    configs[opt] = False
            else:
                configs[opt] = value


def load_default_configs():
    configs["ai"] = "ollama"
    configs["model"] = "llama3.1"
    configs["host"] = "localhost"
    configs["port"] = 11434
    configs["debug"] = False

    configs["level"] = "grade 4 student"
    configs["progress_path"] = "./"
    configs["progress_file"] = "user.progress"
    configs["speech_rate"] = 150
    configs["word_sort_rule"] = "progress"


def load_progress():
    global configs, progress
    path = "{}/{}".format(configs["progress_path"], configs["progress_file"])
    if os.path.exists(path):
        with open(path, "rb") as f:
            progress = pickle.load(f)
    else:
        progress = {
            "total": {},
            "correct": {},
        }


def save_progress():
    global configs, progress
    path = "{}/{}".format(configs["progress_path"], configs["progress_file"])
    with open(path, "wb") as file:
        pickle.dump(progress, file, pickle.HIGHEST_PROTOCOL)


def inc_progress_correct(word):
    progress["correct"][word] = progress["correct"].get(word, 0) + 1


def inc_progress_total(word):
    progress["total"][word] = progress["total"].get(word, 0) + 1
