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
        try:
            winstreak = stats.streak('W')
            losestreak = stats.streak('L')
            if losestreak == 0:
                streak = winstreak
                streak_text = 'winstreak'
            else:
                streak = losestreak
                streak_text = 'losestreak'
            Menu.motd(games, db.db, sport, streak, streak_text)
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
                print(texts["added"])
                db.save()
                input(texts["enter_to_continue"])
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
                            print(texts["game_index_out"])
                            break

                    except ValueError:
                        print("Invalid input.")

                    except Exception as e:
                        print(f'ERROR: {e}')

                input(texts["enter_to_continue"])
                Menu.clear_screen()

            #---show stats---
            elif choice == 3:
                stats.stats_review()
                input(texts["enter_to_continue"])
                Menu.clear_screen()
            
            #---show career highs---
            elif choice == 4:
                stats.highs()
                input(texts["enter_to_continue"])
                Menu.clear_screen()

            #---csv export---
            elif choice == 5:
                export.export(db.sport, False)
                Menu.clear_screen()
            
            # ---courtcv---
            elif choice == 6:
                if sport != 'basketball':
                    print(texts["unavailable_ccv"])
                    input(texts["enter_to_continue"])
                try:
                    choice = int(input(f"[1] - {texts["create_sheet_ccv"]}\n[2] - {texts["generate_ccv"]}\n[Enter] - {texts["back"]}\n>>> "))
                    if choice == 1:
                        print(f'{texts["data_formatting_ccv"]} https://github.com/80degree/CourtCV')
                        code = ccv.create(img=input(f'{texts["img_path_ccv"]}(e.g karl-anthony.png): '), 
                                data=input(f'{texts["data_path_ccv"]}(e.g karl-anthony.json): '), 
                                games_csv=input(f'{texts["games_path_ccv"]}(e.g karl-anthony.csv): '), 
                                output=input(f'{texts["output_format_ccv"]}(pdf/html/both): '))
                        if code == 0:
                            print(f'{texts["finished_export_ccv"]} output')
                        else:
                            input(texts["enter_to_continue"])
                    if choice == 2:
                        export.export(sport, True)
                        print(f'{texts["finished_export_ccv"]} courtcv_input.csv')
                        print(texts["gen_notice_ccv"])
                        input(texts["enter_to_continue"])
                except ValueError:
                    pass
                            
                except Exception as e:
                    print(f'error: {e}')
                    input(texts["enter_to_continue"])

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
            input(texts["enter_to_continue"])
            Menu.clear_screen()

        elif user_choice == 4:
            break


if __name__ == '__main__':
    main()
    db.save()
    sys.exit(0)
