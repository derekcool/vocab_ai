import platform
import pyttsx3


if platform.system() == 'Darwin':
    engine = pyttsx3.init('nsss')
else:
    engine = pyttsx3.init()


def say(text):
    engine.say(text)
    engine.runAndWait()


def set_rate(rate):
    engine.setProperty('rate', rate)


def set_volume(volume):
    engine.setProperty('volume', volume)
