# export_handler is responsible for exporting
import csv
import json
from datetime import datetime
from ui_handler import texts

now = datetime.now()


def export_to_csv(sport, filename=f'export_{now.strftime("%d%m%Y_%H%M%S")}.csv'):
    if sport == 1:
        try:
            with open('basketball.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"{texts["file_not_found"]}: basketball.json")
            input(f'{texts["enter_to_continue"]}...')
            return
        except Exception as e:
            print(f'ERROR: {e}')
            input(f'{texts["enter_to_continue"]}...')
            return

        games = data['games']
        if not games:
            print(f'{texts["no_games"]}')
            return

        headers = ['Date', 'POS', 'MIN', 'PTS', 'AST', '2PTA', '2PTM', '3PTA', '3PTM', 'REB', 'BLK', 'STL', 'PF',
                   'Missed Free Throws', 'Turnovers', 'Result']

        key_mapping = {
            'Date': 'date',
            'POS': 'position',
            'MIN': 'minutes',
            'PTS': 'points',
            'AST': 'assists',
            '2PTA': '2pt_attempts',
            '2PTM': '2pt_shots_made',
            '3PTA': '3pt_attempts',
            '3PTM': '3pt_shots_made',
            'REB': 'rebounds',
            'BLK': 'blocks',
            'STL': 'steals',
            'PF': 'personal_fouls',
            'Missed Free Throws': 'missedFT',
            'Turnovers': 'turnovers',
            'Result': 'Won'
        }

        with open(filename, 'w', newline='', encoding='utf-8') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=headers)
            writer.writeheader()
            for game in games:
                row = {csv_key: game.get(json_key, '') for csv_key, json_key in key_mapping.items()}
                writer.writerow(row)

    if sport == 2:
        try:
            with open('soccer.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"{texts["file_not_found"]}: soccer.json")
            input(f'{texts["enter_to_continue"]}...')
            return
        except Exception as e:
            print(f'ERROR: {e}')
            input(f'{texts["enter_to_continue"]}...')
            return

        games = data['games']
        if not games:
            print(f'{texts["no_games"]}')
            return

        headers = ['Date', 'POS', 'MIN', 'GOALS', 'AST', 'SHOTS', 'Yellow cards', 'Red cards', 'Fouls', 'Result']

        key_mapping = {
            'Date': 'date',
            'POS': 'position',
            'MIN': 'minutes',
            'GOALS': 'goals',
            'AST': 'assists',
            'SHOTS': 'shots',
            'Yellow cards': 'yellow_cards',
            'Red cards': 'red_cards',
            'Fouls': 'fouls',
            'Result': 'Won'
        }

        with open(filename, 'w', newline='', encoding='utf-8') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=headers)
            writer.writeheader()
            for game in games:
                row = {csv_key: game.get(json_key, '') for csv_key, json_key in key_mapping.items()}
                writer.writerow(row)

    print(f'{texts["export_finished"]} {filename}')
    input(f'{texts["enter_to_continue"]}...')
