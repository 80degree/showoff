# statistics_handler is responsible for displaying stats
import data_handler
from ui_handler import texts

db = data_handler
games = data_handler.db["games"]
sport = db.sport


def stats_review():
    if sport == 1:
        all_points = sum(game["points"] for game in games)
        all_minutes = sum(game["minutes"] for game in games)
        all_2pt = sum(game["2pt_shots_made"] for game in games)
        all_3pt = sum(game["3pt_shots_made"] for game in games)
        all_assists = sum(game["assists"] for game in games)
        all_rebounds = sum(game["rebounds"] for game in games)
        all_blocks = sum(game["blocks"] for game in games)
        all_steals = sum(game["steals"] for game in games)
        all_missed = (sum(game["3pt_attempts"] for game in games) - all_3pt) + (sum(game["2pt_attempts"] for game in games) - all_2pt)
        all_turnovers = sum(game["turnovers"] for game in games)
        all_missed_free_throws = sum(game["missed_free_throws"] for game in games)
        all_games = len(games)
        efficiency = calculate_efficiency(all_points, all_rebounds, all_assists, all_steals, all_blocks, all_missed, all_turnovers, all_missed_free_throws)

        if all_games == 0:
            print(f"{texts["no_saved_games"]}.")
            return 
    
        table = [[texts["game_points"], all_points, round(all_points / all_games, 2)], [texts["game_minutes"], all_minutes, round(all_minutes / all_games, 2)],
                [texts["game_2pt"], all_2pt, round(all_2pt / all_games, 2)], [texts["game_3pt"], all_3pt, round(all_3pt / all_games, 2)],
                [texts["game_assists"], all_assists, round(all_assists / all_games, 2)], [texts["game_rebounds"], all_rebounds, round(all_rebounds / all_games, 2)],
                [texts["game_blocks"], all_blocks, round(all_blocks / all_games, 2)], [texts["game_steals"], all_steals, round(all_steals / all_games, 2)],
                [texts["game_missed"], all_missed, round(all_missed / all_games, 2)], [texts["game_missed_free_throws"], all_missed_free_throws, round(all_missed_free_throws / all_games, 2)]
                ]

        print(f"{f'{texts["stat"]}':<20} {f'{texts["all_time"]}':<10} {f'{texts["per_game"]}'}")
        print("─" * 40)
        for stat, ag, pg in table:
            print(f"{stat:<20} {ag:<10} {pg}")
        print("─" * 40)
        print(f"{texts["games"]}: {all_games}\n{texts["efficiency"]}: {efficiency}")
        print("─" * 40)
    
    elif sport == 2:
        all_minutes = sum(game["minutes"] for game in games)
        all_goals = sum(game["goals"] for game in games)
        all_assists = sum(game["assists"] for game in games)
        all_shots = sum(game["shots"] for game in games)
        all_saves = sum(game["saves"] for game in games)
        all_steals = sum(game["steals"] for game in games)
        all_yellow_cards = sum(game["yellow_cards"] for game in games)
        all_red_cards = sum(game["red_cards"] for game in games)
        all_games = len(games)
        
        if all_games == 0:
            print(f"{texts["no_saved_games"]}.")
            return
        
        table = [["Minutes", all_minutes, None], ["Goals", all_goals, round(all_goals / all_games, 2)],
                ["Assists", all_assists, round(all_assists / all_games, 2)], ["Shots", all_shots, round(all_shots / all_games, 2)],
                ["Saves", all_saves, round(all_saves / all_games, 2)], ["Steals", all_steals, round(all_steals / all_games, 2)],
                ["Yellow Cards", all_yellow_cards, round(all_yellow_cards / all_games, 2)], ["Red Cards", all_red_cards, round(all_red_cards / all_games, 2)]
                ]
        
        print(f"{f'{texts["stat"]}':<20} {f'{texts["all_time"]}':<10} {f'{texts["per_game"]}'}")
        print("─" * 40)
        for stat, ag, pg in table:
            print(f"{stat:<20} {ag:<10} {pg}")
        print("─" * 40)
        print(f"{texts["games"]}: {all_games}")
        print("─" * 40)


def calculate_efficiency(points, rebounds, assists, steals, blocks, missed, missed_free_throws, turnovers):
    efficiency = (points + rebounds + assists + steals + blocks) - (missed + missed_free_throws + turnovers)
    return efficiency


def show_stats(match_index):
    print(f'{texts["player"]}: {data_handler.db["player"]}')
    print(f'{texts["name"]}: {games[match_index]["name"]}')
    print(f'{texts["date"]}: {games[match_index]["date"]}')
    print(f'Opponent: {games[match_index]["opponent"]}')
    print("─" * 35)
    if sport == 1:
        table = [[texts["game_points"], str(games[match_index]["points"])], [texts["game_minutes"], str(games[match_index]["minutes"])],
                 [texts["game_2pt"], f'{str(games[match_index]["2pt_shots_made"])}/{str(games[match_index]["2pt_attempts"])}'], [texts["game_3pt"], f'{str(games[match_index]["3pt_shots_made"])}/{str(games[match_index]["3pt_attempts"])}'],
                 [texts["game_assists"], str(games[match_index]["assists"])], [texts["game_rebounds"], str(games[match_index]["rebounds"])],
                 [texts["game_blocks"], str(games[match_index]["blocks"])], [texts["game_steals"], str(games[match_index]["steals"])],
                 [texts["game_personal_fouls"], str(games[match_index]["personal_fouls"])], [texts["game_missed_free_throws"], str(games[match_index]["missed_free_throws"])],
                 [texts["game_turnovers"], str(games[match_index]["turnovers"])], [texts["game_result"], str(games[match_index]["result"])]
                 ]
        print(f"{f'{texts["stat"]}':<20} {f'{texts["value"]}'}")
        print("─" * 35)
        for stat, value in table:
            print(f"{stat:<20} {value}")
        print("─" * 35)

    if sport == 2:
        table = [[texts["game_minutes"], str(games[match_index]["minutes"])], [texts["game_goals"], str(games[match_index]["goals"])],
                 [texts["game_assists"], str(games[match_index]["assists"])], [texts["game_shots"], str(games[match_index]["shots"])],
                 [texts["game_saves"], str(games[match_index]["saves"])], [texts["game_steals"], str(games[match_index]["steals"])],
                 [texts["game_yellow_cards"], str(games[match_index]["yellow_cards"])], [texts["game_red_cards"], str(games[match_index]["red_cards"])],
                 [texts["game_result"], str(games[match_index]["result"])]
                 ]
        print(f"{f'{texts["stat"]}':<20} {f'{texts["value"]}'}")
        print("─" * 35)
        for stat, value in table:
            print(f"{stat:<20} {value}")
        print("─" * 35)

def highs():
    if sport == 1:
        print('CAREER HIGHS')
        table = [[texts["game_points"], max(game["points"] for game in games)], [texts["game_minutes"], max(game["minutes"] for game in games)],
                [texts["game_2pt"], f'{max(game["2pt_shots_made"] for game in games)}/{max(game["2pt_attempts"] for game in games)}'], [texts["game_3pt"], f'{max(game["3pt_shots_made"] for game in games)}/{max(game["3pt_attempts"] for game in games)}'],
                [texts["game_assists"], max(game["assists"] for game in games)], [texts["game_rebounds"], max(game["rebounds"] for game in games)],
                [texts["game_blocks"], max(game["blocks"] for game in games)], [texts["game_steals"], max(game["steals"] for game in games)],
                [texts["game_personal_fouls"], max(game["personal_fouls"] for game in games)], [texts["game_missed_free_throws"], max(game["missed_free_throws"] for game in games)],
                [texts["game_turnovers"], max(game["turnovers"] for game in games)], ["Wins", sum(g["result"] == "W" for g in games)], ["Losses", sum(g["result"] == "L" for g in games)]
                ]
        print(f"{f'{texts["stat"]}':<20} {f'{texts["value"]}'}")
        print("─" * 35)
        for stat, value in table:
            print(f"{stat:<20} {value}")
        print("─" * 35)
    
    if sport == 2:
        pass

def streak(result):
    streak = 0
    for g in games:
        streak = streak + 1 if g["result"] == result else 0
    return streak