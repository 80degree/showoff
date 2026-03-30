import os
import json

from __init__ import INFO, RUNNING_DIR

while True:
    try:
        with open(f'{RUNNING_DIR}/preferences.json', 'r', encoding='utf-8') as f:
            preferences = json.load(f)
            lang = preferences['lang']
        break
    except FileNotFoundError:
        with open(f'{RUNNING_DIR}/preferences.json', 'w', encoding='utf-8') as f:
            try:
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
            except ValueError:
                print("Invalid input")

with open(f'{RUNNING_DIR}/locales/lang_{lang}.json', 'r', encoding='utf-8') as f:
    texts = json.load(f)

MENU = f"""
[1] - {texts["games_menu"]}
[2] - {texts["settings"]}
[3] - {texts["about"]}
[4] - {texts["exit"]}
"""

SETTINGS_MENU = f"""
[1] - {texts["change_lang"]}
[2] - {texts["change_sport"]}
[Enter] - {texts["back"]}
"""

GAMES_MENU = f"""
[1] - {texts["add_game"]}
[2] - {texts["view_games"]}
[3] - {texts["stats_review"]}
[4] - {texts["career_highs"]}
[5] - {texts["data_export"]}
[6] - CourtCV - {texts["courtcv"]}
[Enter] - {texts["back"]}
"""

DESCRIPTION = f"{texts["description"]}\nhttps://github.com/80degree/showoff\nUses CourtCV https://github.com/80degree/CourtCV"

def change_lang(preferences, lang):
    with open(f'{RUNNING_DIR}/preferences.json', 'w', encoding='utf-8') as f:
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
            print(INFO + DESCRIPTION)

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

    @staticmethod
    def games_menu():
        try:
            print(GAMES_MENU)
            choice = int(input(f"{texts["select"]} >> "))
            return choice
        except ValueError:
            choice = ValueError
            return choice
        except Exception as e:
            print(f'ERROR: {e}')
    
    @staticmethod
    def motd(games, db, sport, current_streak, streak_text):
        print(f"{texts["currently_in"]} {sport}")
        print(f"{texts['welcome_back']}, {db['player']}\n{texts['games_played']}: {len(games)}.\n{texts['last_game']}: {games[-1]['date']}, {texts['game_points']}: {games[-1]['points']}. {texts['keep_up']}!")
        print(f"{texts['your_streak']} {current_streak} {texts[streak_text]}.")