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
    configs["level"] = "grade 4 student"
    configs["model"] = "llama3.1"
    configs["debug"] = False
    configs["host"] = "localhost"
    configs["port"] = 11434
    configs["progress_path"] = "./"
    configs["progress_file"] = "user.progress"


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
    print(progress)

def save_progress():
    global configs, progress
    path = "{}/{}".format(configs["progress_path"], configs["progress_file"])
    with open(path, "wb") as file:
        pickle.dump(progress, file, pickle.HIGHEST_PROTOCOL)

