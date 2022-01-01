import random
import os
import time

from gtts import gTTS
from termcolor import cprint
from pyfiglet import figlet_format

LANG = "pt"

def create_bingo(ran):
    sorteio = random.sample(range(1,ran+1), ran)
    return [str(i) for i in sorteio ]


def print_num(num):
    cprint(figlet_format(string, font='starwars'))


def say_numbers(string_list):
    for string in string_list:
        print_num(string)
        obj = gTTS(string, lang=LANG, slow = True)
        obj.save("num.mp3")
        os.system("mpv num.mp3")
        time.sleep(4)
        os.system("mpv num.mp3")


def import_or_install(package):
    try:
        __import__(package)
    except ImportError
        pip.main(['install', package]


sorteio=create_bingo(90)
say_numbers(sorteio)
obj2 = gTTS("Acabou pudins", lang=LANG, slow = True)
obj2.save("num.mp3")
os.system("mpv num.mp3")
