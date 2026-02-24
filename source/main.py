try:
    import data_handler
    import ui_handler
    import os
    import sys
    from ui_handler import Menu
    import statistics_handler
    import export_handler
except FileNotFoundError:
    print('Some files were not found. The program will not run, try to redownload the program or open an issue, if reinstalling didnt help')
    input(f'{ui_handler.texts["enter_to_continue"]}')
except ModuleNotFoundError as e:
    print(f'Some modules were not installed on your computer.\n Error:{e}')
    input(f'{ui_handler.texts["enter_to_continue"]}')

db = data_handler
ui = ui_handler
stats = statistics_handler
games = data_handler.db["games"]
export = export_handler
texts = ui.texts

if db.sport == 1:
    sport = 'basketball'
elif db.sport == 2:
    sport = 'soccer'

def main():
    while True:
        Menu.show_info(False)
        print(f"{texts["currently_in"]} {sport}")
        user_choice = Menu.create_menu()

        if user_choice == 1:
            db.add_match()
            print(f"{texts["added"]}")
            db.save()
            input(f"{texts["enter_to_continue"]}... ")
            Menu.clear_screen()

        elif user_choice == 2:
            gamescount = len(games)
            for i in range(gamescount):
                print(f"{i + 1} - {str(games[i]['name'])}")
            choice = input(f"{texts["game_to_show"]}\n")
            if choice != '' and int(choice) - 1 in range(gamescount):
                stats.show_stats(int(choice) - 1)
            else:
                print(f"{texts["game_index_out"]}.")
            input(f"{texts["enter_to_continue"]}... ")
            Menu.clear_screen()

        elif user_choice == 3:
            stats.stats_review()
            input(f"{texts["enter_to_continue"]}... ")
            Menu.clear_screen()

        elif user_choice == 4:
            export.export_to_csv(db.sport)
            Menu.clear_screen()

        elif user_choice == 5:
            os.execl(sys.executable, sys.executable, *sys.argv)

        elif user_choice == 6:
            Menu.clear_screen()
            Menu.show_info(True)
            input(f"{texts["enter_to_continue"]}... ")
            Menu.clear_screen()

        elif user_choice == 7:
            os.execl(sys.executable, sys.executable,  *sys.argv)

        elif user_choice == 8:
            break


if __name__ == '__main__':
    main()
    db.save()
    sys.exit(0)
