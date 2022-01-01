import random
import os
import time
import pip

from gtts import gTTS
from termcolor import cprint
from pyfiglet import figlet_format


LANG = "pt"
MP3_player = "mpv"


def create_bingo(ran):
    sorteio = random.sample(range(1,ran+1), ran)
    return [str(i) for i in sorteio ]


def print_num(string):
    cprint(figlet_format(string, font='starwars'))


def say_numbers(string_list):
    for string in string_list:
        print_num(string)
        obj = gTTS(string, lang=LANG, slow = True)
        obj.save("num.mp3")
        #repeat twice with 4 second interval
        os.system(f"{MP3_player} num.mp3")
        time.sleep(4)
        os.system(f"{MP3_player} num.mp3")
        time.sleep(2)


def setup(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


if __name__=="__main__":
    for pkg in ["gtts", "cprint", "pyfiglet"]:
        setup(pkg)
    sorteio=create_bingo(90)
    say_numbers(sorteio)
    os.system("rm num.mp3")
