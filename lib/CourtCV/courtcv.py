# Modified. See original at https://github.com/80degree/CourtCV
'''CourtCV
Author: worthyworm
Year: 2026
Licesed under the GPLv3 License
'''
import json
import csv
from __init__ import RUNNING_DIR

def create(img, data, games_csv, output='html'):
    if output == 'pdf' or output == 'both':
        try:
            from weasyprint import HTML
        except ImportError:
            print('Weasyprint is not installed. Please install it to use the pdf output(pip install weasyprint).')
            output = 'html'
    games = []

    with open(f'{RUNNING_DIR}/{games_csv}', newline='') as f:
        #print('reading')
        reader = csv.DictReader(f)
        for row in reader:
            games.append(row)


    with open(f'{RUNNING_DIR}/lib/CourtCV/template.html', 'r') as f:
        template = f.read()

    with open(f'{RUNNING_DIR}/{data}', 'r') as f:
        data = json.load(f)

    #calculating the statistics
    ppg = sum(int(g['pts']) for g in games) / len(games)
    #print(ppg)
    rpg = sum(int(g['reb']) for g in games) / len(games)
    #print(rpg)
    apg = sum(int(g['ast']) for g in games) / len(games)
    #print(apg)

    #replacing the placeholders
    html = template.replace('{{player_name}}', data["name"])
    html = html.replace('{{player_img}}', img)
    html = html.replace('{{position}}', data["position"])
    html = html.replace('{{height}}', data["height"])
    html = html.replace('{{team}}', data["team"])
    html = html.replace('{{season}}', data["season"])
    html = html.replace('{{fg_pct}}', data["fg_pct"])
    html = html.replace('{{ppg}}', str(ppg))
    html = html.replace('{{rpg}}', str(rpg))
    html = html.replace('{{apg}}', str(apg))

    #adding games
    rows_html = "\n".join([
        f"""<tr>
            <td>{g['date']}</td>
            <td>{g['opponent']}</td>
            <td>{g['pts']}</td>
            <td>{g['reb']}</td>
            <td>{g['ast']}</td>
            <td>{g['min']}</td>
        </tr>"""
        for g in games
    ])
    html = html.replace('{{game_rows}}', rows_html)

    try:
        if output == 'pdf':
            html = HTML(string=html, base_url='.').write_pdf('output.pdf')
            return 0
        elif output == 'both':
            html = HTML(string=html, base_url='.').write_pdf('output.pdf')
            with open('output.html', 'w') as f:
                f.write(html)
            return 0
        else:
            with open(f'output.html', 'w') as f:
                f.write(html)
            return 0
    except Exception as e:
        print(f'error: {e}')
        return 1