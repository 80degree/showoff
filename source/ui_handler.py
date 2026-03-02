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
                json.dump({"lang": lang}, f, ensure_ascii=False, indent=4)
                break
            elif lang == 2:
                lang = 'ru'
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
[5] - {texts["settings"]}
[6] - {texts["about"]}
[7] - {texts["exit"]}
"""

SETTINGS_MENU = f"""
[1] - {texts["change_lang"]}
[2] - {texts["change_sport"]}
[3] - {texts["back"]}
"""

DESCRIPTION = f"{texts["description"]}\nhttps://github.com/worthyworm/showoff"

def change_lang(preferences, lang):
    with open('preferences.json', 'w', encoding='utf-8') as f:
        if lang == 'en':
            preferences['lang'] = 'ru'
            json.dump(preferences, f, ensure_ascii=False, indent=4)
            print("Язык изменен на русский.")
            input("Enter чтобы продолжить...")
        elif lang == 'ru':
            preferences['lang'] = 'en'
            json.dump(preferences, f, ensure_ascii=False, indent=4)
            print("Language set to English.")
            input("Enter to continue...")

class Menu:

    @staticmethod
    def create_menu():
        print(MENU)
        try:
            choice = int(input(f"{texts["select"]} >> "))
            return choice
        except ValueError:
            choice = ValueError
            return choice
        except Exception as e:
            print(f'ERROR: {e}')

    @staticmethod
    def show_info(full):
        if not full:
            print(INFO)
        else:
            print(INFO, DESCRIPTION)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def settings_menu():
        try:
            print(SETTINGS_MENU)
            choice = int(input(f"{texts["select"]} >> "))
            return choice
        except ValueError:
            choice = ValueError
            return choice
        except Exception as e:
            print(f'ERROR: {e}')