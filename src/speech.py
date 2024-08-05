import platform


is_mac = platform.system() == 'Darwin'

if is_mac:
    import subprocess
else:
    import pyttsx3
    engine = pyttsx3.init()
    # engine = pyttsx3.init('nsss')


def say(text):
    if is_mac:
        subprocess.run(['say', text])
    else:
        engine.say(text)
        engine.runAndWait()


def set_rate(rate):
    if not is_mac:
        engine.setProperty('rate', rate)


def set_volume(volume):
    if not is_mac:
        engine.setProperty('volume', volume)
