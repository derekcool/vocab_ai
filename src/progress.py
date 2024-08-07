import pickle
import os.path
import myconfigs


progress = {}
progress_filepath = None


def load_progress(filepath):
    global progress, progress_filepath
    progress_filepath = filepath
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            progress = pickle.load(f)
    else:
        progress = {
            "total": {},
            "correct": {},
        }


def save_progress():
    global progress, progress_filepath
    if progress_filepath is None:
        print("Error: progress filepath is not set.")
        return
    # path = "{}/{}".format(myconfigs.configs["progress_path"], myconfigs.configs["progress_file"])
    print("saving progress to", progress_filepath)
    with open(progress_filepath, "wb") as file:
        pickle.dump(progress, file, pickle.HIGHEST_PROTOCOL)
        print("progress saved")


def inc_progress_correct(word):
    progress["correct"][word] = progress["correct"].get(word, 0) + 1


def inc_progress_total(word):
    progress["total"][word] = progress["total"].get(word, 0) + 1


def get_progress_total(word):
    return progress["total"].get(word, 0)


def get_progress_correct(word):
    return progress["correct"].get(word, 0)

