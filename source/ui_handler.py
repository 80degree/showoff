import os
import json

from __init__ import INFO

while True:
    try:
        with open('preferences.json', 'r', encoding='utf-8') as f:
            preferences = json.load(f)
            lang = preferences['lang']
        break
    except FileNotFoundError:
        with open('preferences.json', 'w', encoding='utf-8') as f:
            lang = int(input("[1] - English\n[2] - Русский\n>>>"))
            if lang == 1:
                lang = 'en'
                with open('preferences.json', 'w', encoding='utf-8') as f:
                    json.dump({"lang": lang}, f, ensure_ascii=False, indent=4)
                break
            elif lang == 2:
                lang = 'ru'
                with open('preferences.json', 'w', encoding='utf-8') as f:
                    json.dump({"lang": lang}, f, ensure_ascii=False, indent=4)
                break
            else:
                print("Out of range.")


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
        if not full:
            print(INFO)
        else:
            print(INFO, DESCRIPTION)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
