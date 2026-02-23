import json
from ui_handler import texts

sport = int(input(f'''
{texts["select_sport"]}:
[1] - {texts["basketball"]}
[2] - {texts["soccer"]}
'''))
if sport == 1:
    try:
        with open('basketball.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
    except FileNotFoundError:
        player = input(f"{texts["enter_name"]}: ")
        db = {"player": player, "games": []}
    except Exception as e:
        print(f'ERROR: {e}')

elif sport == 2:
    try:
        with open('soccer.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
    except FileNotFoundError:
        player = input(f'{texts["enter_name"]}: ')
        db = {"player": player, "games": []}
    except Exception as e:
        print(f'ERROR: {e}')



def add_match():
    if sport == 1:
        new_game = {
            "name": input(f"{texts["game_name"]}: "),
            "date": input(f"{texts["game_date"]}: "),
            "position": input(f'{texts["game_position"]}: '),
            "minutes": int(input(f'{texts["game_minutes"]}: ')),
            "points": int(input(f"{texts["game_points"]}: ")),
            "assists": int(input(f"{texts["game_assists"]}: ")),
            "2pt_attempts": int(input(f'{texts["game_2pta"]}: ')),
            "3pt_attempts": int(input(f'{texts["game_3pta"]}: ')),
            "2ptshots_made": int(input(f'{texts["game_2ptm"]}: ')),
            "3ptshots_made": int(input(f'{texts["game_3ptm"]}: ')),
            "rebounds": int(input(f"{texts["game_rebounds"]}: ")),
            "blocks": int(input(f"{texts["game_blocks"]}: ")),
            "steals": int(input(f"{texts["game_steals"]}: ")),
            "personal_fouls": int(input(f"{texts["game_personalfouls"]}: ")),
            "missedFT": int(input(f"{texts["game_missedFT"]}: ")),
            "turnovers": int(input(f"{texts["game_turnovers"]}: ")),
            "Won": input(f"{texts["game_result"]}: ")
        }
    
    elif sport == 2:
        new_game = {
            "name": input(f"{texts["game_name"]}: "),
            "date": input(f"{texts["game_date"]}: "),
            "position": input(f'{texts["game_position"]}: '),
            "minutes": int(input(f'{texts["game_minutes"]}: ')),
            "goals": int(input(f'{texts["game_goals"]}: ')),
            "assists": int(input(f'{texts["game_assists"]}: ')),
            "shots": int(input(f'{texts["game_shots"]}: ')),
            "yellow_cards": int(input(f"{texts["game_yellowcards"]}: ")),
            "red_cards": int(input(f'{texts["game_redcards"]}: ')),
            "fouls": int(input(f'{texts["game_personalfouls"]}: ')),
            "Won": input(f"{texts["game_result"]}: ")
        }
    
    db["games"].append(new_game)


def save():
    if sport == 1:
        with open('basketball.json', 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)
    if sport == 2:
        with open('soccer.json', 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)
