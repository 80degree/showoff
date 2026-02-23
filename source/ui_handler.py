import os
import json
import sys

from __init__ import INFO

lang = int(input("[1] - English\n[2] - Русский\n>>>"))
if lang == 1:
    lang = 'en'
elif lang == 2:
    lang = 'ru'
else:
    print("Out of range.")
    os.execv(sys.executable, ['python'] + sys.argv)

with open(f'locales/lang_{lang}.json', 'r', encoding='utf-8') as f:
    texts = json.load(f)

MENU = f"""
[1] - {texts["add_game"]}
[2] - {texts["view_games"]}
[3] - {texts["stats_review"]}
[4] - {texts["data_export"]}
[5] - {texts["change_sport"]}
[6] - {texts["about"]}
[7] - {texts["change_lang"]}
[8] - {texts["exit"]}

"""

DESCRIPTION = f"{texts["description"]}\nhttps://github.com/worthyworm/showoff"

class Menu:

    @staticmethod
    def create_menu():
        print(MENU)
        choice = int(input(f"{texts["select"]} >> "))
        return choice

    @staticmethod
    def show_info(full):
        if full == False:
            print(INFO)
        else:
            print(INFO, DESCRIPTION)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
