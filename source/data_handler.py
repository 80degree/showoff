# data_handler is responsible for the operations with db and json's
import json
import sys
from ui_handler import texts
from __init__ import VERSION

while True:
    try:
        sport = int(input(f'''
{texts["select_sport"]}:
[1] - {texts["basketball"]}
[2] - {texts["soccer"]}
>>>'''))
        if sport > 2 or sport < 1:
            print("Invalid option")
        else:
            break
    except ValueError:
        print('Invalid input')
        input(f'{texts["enter_to_continue"]}')

    except Exception as e:
        print(f'ERROR: {e}')
        input(f'Press enter to exit...')
        sys.exit(1)

positions_basketball = ['PG', 'SG', 'SF', 'PF', 'C']
positions_soccer = ['GK', 'SW', 'LB', 'CB', 'RB', 'LWB', 'RWB', 'DM', 'LM', 'CM', 'RM', 'AM', 'LW', 'SS', 'RW', 'LF', 'CF', 'RF']
#positions_voleyball = ['OH', 'OPP', 'MB', 'S', 'L', 'DS', 'SS']

if sport == 1:
    try:
        with open('basketball.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
            if tuple(map(int, db['version'].split('.'))) < (1, 1, 2):
                print(f'{texts["unsupported_version"]}: {db["version"]}version')
                input('Enter to continue')
                sys.exit(1)
    except FileNotFoundError:
        player = input(f"{texts["enter_name"]}: ")
        db = {"version": VERSION, "player": player, "games": []}
    except json.decoder.JSONDecodeError as e:
        print(f"The file is not a valid Json file or is empty\nERROR: {e}")
        input(f'{texts["enter_to_continue"]}')
        sys.exit(1)
    except Exception as e:
        print(f'ERROR: {e}')
        input(f'{texts["enter_to_continue"]}')
        sys.exit(1)

elif sport == 2:
    try:
        with open('soccer.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
            if tuple(map(int, db['version'].split('.'))) < (1, 1, 2):
                print(f'{texts["unsupported_version"]}: {db["version"]}')
                input('Enter to continue')
                sys.exit(1)
    except FileNotFoundError:
        player = input(f'{texts["enter_name"]}: ')
        db = {"version": VERSION, "player": player, "games": []}
    except Exception as e:
        print(f'ERROR: {e}')
        input(f'{texts["enter_to_continue"]}')
        sys.exit(1)


def add_match():
    if sport == 1:
        while True:
            try:
                new_game = {
                    "name": input(f"{texts["game_name"]}: "),
                    "date": input(f"{texts["game_date"]}: "),
                    "position": positions_basketball[int(input(f'{texts["game_basketball_position"]}\n>>> ').strip()) - 1],
                    "minutes": int(input(f'{texts["game_minutes"]}: ')),
                    "points": int(input(f"{texts["game_points"]}: ")),
                    "assists": int(input(f"{texts["game_assists"]}: ")),
                    "2pt_attempts": int(input(f'{texts["game_2pta"]}: ')),
                    "3pt_attempts": int(input(f'{texts["game_3pta"]}: ')),
                    "2pt_shots_made": int(input(f'{texts["game_2ptm"]}: ')),
                    "3pt_shots_made": int(input(f'{texts["game_3ptm"]}: ')),
                    "rebounds": int(input(f"{texts["game_rebounds"]}: ")),
                    "blocks": int(input(f"{texts["game_blocks"]}: ")),
                    "steals": int(input(f"{texts["game_steals"]}: ")),
                    "personal_fouls": int(input(f"{texts["game_personal_fouls"]}: ")),
                    "missed_free_throws": int(input(f"{texts["game_missed_free_throws"]}: ")),
                    "turnovers": int(input(f"{texts["game_turnovers"]}: ")),
                    "result": input(f"{texts["game_result"]}: ")
                }
                break
            except ValueError:
                print(f'Invalid input')
                input(f'{texts["enter_to_continue"]}')

            except IndexError:
                print('Out of range')
                input(f'{texts["enter_to_continue"]}')

            except Exception as e:
                print(f'ERROR: {e}')
                input(f'{texts["enter_to_continue"]}')
                sys.exit(1)
    
    elif sport == 2:
        while True:
            try:
                new_game = {
                    "name": input(f"{texts["game_name"]}: "),
                    "date": input(f"{texts["game_date"]}: "),
                    "position": positions_soccer[int(input(f'{texts["game_soccer_position"]}\n>>> ').strip()) - 1],
                    "minutes": int(input(f'{texts["game_minutes"]}: ')),
                    "goals": int(input(f'{texts["game_goals"]}: ')),
                    "assists": int(input(f'{texts["game_assists"]}: ')),
                    "saves": int(input(f'{texts["game_saves"]}: ')),
                    "steals": int(input(f'{texts["game_steals"]}: ')),
                    "shots": int(input(f'{texts["game_shots"]}: ')),
                    "yellow_cards": int(input(f"{texts["game_yellow_cards"]}: ")),
                    "red_cards": int(input(f'{texts["game_red_cards"]}: ')),
                    "fouls": int(input(f'{texts["game_personal_fouls"]}: ')),
                    "result": input(f"{texts["game_result"]}: ")
                }
                break
            except ValueError:
                print('Invalid input')
                input(f'{texts["enter_to_continue"]}')

            except Exception as e:
                print(f'ERROR: {e}')
                input(f'{texts["enter_to_continue"]}')
                sys.exit(1)
    
    db["games"].append(new_game)


def save():
    if sport == 1:
        try:
            with open('basketball.json', 'w', encoding='utf-8') as f:
                json.dump(db, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print('File basketball.json does not exist.')
            input(f'{texts["enter_to_continue"]}')
        except Exception as e:
            print(f'ERROR: {e}')
            input(f'{texts["enter_to_continue"]}')
    if sport == 2:
        try:
            with open('soccer.json', 'w', encoding='utf-8') as f:
                json.dump(db, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print('File soccer.json does not exist.')
            input(f'{texts["enter_to_continue"]}')
        except Exception as e:
            print(f'ERROR: {e}')
            input(f'{texts["enter_to_continue"]}')
