import os
import sys
try:
    import data_handler
    import ui_handler
    from ui_handler import Menu
    import statistics_handler
    import export_handler
    import lib.CourtCV.courtcv
except FileNotFoundError as e:
    print('Some files were not found. The program will not run, try to redownload the program or open an issue, if reinstalling didnt help')
    print(f'Некоторые файлы не были найдены. Программа не запустится, попробуйте переустановить или откройте тикет на github.\nERROR: {e}')
    input('Enter to continue...')
    sys.exit(1)
except ModuleNotFoundError as e:
    print(f'Some modules are not installed on your computer.')
    print(f'Некоторые модули не установлены.\nERROR:{e}')
    input('Enter to continue...')
    sys.exit(1)

ccv = lib.CourtCV.courtcv
db = data_handler
ui = ui_handler
stats = statistics_handler
games = data_handler.db["games"]
export = export_handler
texts = ui.texts
preferences = data_handler.preferences

if db.sport == 1:
    sport = 'basketball'
elif db.sport == 2:
    sport = 'soccer'

def main():
    while True:
        Menu.show_info(False)
        print(f"{texts["currently_in"]} {sport}")
        try:
            print(f"{texts['welcome_back']}, {data_handler.db['player']}\n{texts['games_played']}: {len(games)}.\n{texts['last_game']}: {games[-1]['date']}, {texts['game_points']}: {games[-1]['points']}. {texts['keep_up']}!")
        except IndexError:
            pass
        user_choice = Menu.create_menu()
        if user_choice == ValueError:
            Menu.clear_screen()
            pass

        #---games menu---
        if user_choice == 1:
            print(f'{texts["games_menu"]}:')
            choice = Menu.games_menu()

            if choice == ValueError:
                Menu.clear_screen()
                pass

            #---games addition---
            if choice == 1:
                db.add_match()
                print(f"{texts["added"]}")
                db.save()
                input(f"{texts["enter_to_continue"]}... ")
                Menu.clear_screen()

            #---game viewing---
            elif choice == 2:
                games_count = len(games)
                for i in range(games_count):
                    print(f"{i + 1} - {str(games[i]['name'])}")
                while True:
                    try:
                        choice = input(f"{texts["game_to_show"]}\n")
                        if choice != '' and int(choice) - 1 in range(games_count):
                            stats.show_stats(int(choice) - 1)
                            break
                        else:
                            print(f"{texts["game_index_out"]}.")
                            break

                    except ValueError:
                        print("Invalid input.")

                    except Exception as e:
                        print(f'ERROR: {e}')

                input(f"{texts["enter_to_continue"]}... ")
                Menu.clear_screen()

            #---show stats---
            elif choice == 3:
                stats.stats_review()
                input(f"{texts["enter_to_continue"]}... ")
                Menu.clear_screen()

            #---csv export---
            elif choice == 4:
                export.export_to_csv(db.sport)
                Menu.clear_screen()
            
            # ---courtcv---
            elif choice == 5:
                print(f'{texts["data_formatting"]} https://github.com/80degree/CourtCV')
                code = ccv.create(img=input(f'{texts["img_path"]}(e.g karl-anthony.png): '), 
                           data=input(f'{texts["data_path"]}(e.g karl-anthony.json): '), 
                           games_csv=input(f'{texts["games_path"]}(e.g karl-anthony.csv): '), 
                           output=input(f'{texts["output_format"]}(pdf/html/both): '))
                if code == 0:
                    print(texts["added"])
                else:
                    print(texts["enter_to_continue"])

        #---settings menu---
        elif user_choice == 2:
            print(f'{texts["settings"]}:')
            choice = Menu.settings_menu()

            #---language changing---
            if choice == 1:
                ui_handler.change_lang(preferences, ui_handler.lang)
                db.save()
                os.execl(sys.executable, sys.executable, *sys.argv)

            #---sport changing---
            elif choice == 2:
                db.change_sport(preferences)
                db.save()
                os.execl(sys.executable, sys.executable, *sys.argv)
            
            elif choice == ValueError:
                pass

        elif user_choice == 3:
            Menu.clear_screen()
            Menu.show_info(True)
            input(f"{texts["enter_to_continue"]}... ")
            Menu.clear_screen()

        elif user_choice == 4:
            break


if __name__ == '__main__':
    main()
    db.save()
    sys.exit(0)
