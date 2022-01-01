import os
import random
import time
import vlc

from gtts import gTTS
from termcolor import cprint
from pyfiglet import figlet_format


LANG = "pt"
SOUND_FILE = "temp.mp3"


def create_lotto(ran):
    """
    gets a list with a random, non repeating sample
    """
    lotto = random.sample(range(1,ran+1), ran)
    return [str(num) for num in lotto ]


def print_num(string):
    """
    prett prints the number in the console
    """
    cprint(figlet_format(string, font='starwars'))


def say_numbers(string_list):
    """
    gets a list of strings, prints and recites them.
    """
    for string in string_list:
        print_num(string)
        obj = gTTS(string, lang=LANG, slow=True)
        obj.save(SOUND_FILE)
        play_sounds(SOUND_FILE)


def play_sounds(sound_file):
    """
    plays the sound twice, separated by 4 seconds each time.
    """
    for sound in range(2):
        play_sound = vlc.MediaPlayer(sound_file)
        play_sound.play()
        time.sleep(3)


if __name__=="__main__":
    lotto = create_lotto(90)
    say_numbers(lotto)
    # cleanup
    os.unlink("num.mp3")
