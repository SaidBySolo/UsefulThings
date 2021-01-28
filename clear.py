import os
import platform


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
        return
    elif platform.system() == 'Windows':
        os.system('cls')
        return
