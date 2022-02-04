import PySimpleGUI as sg
import random

#todo: not in words list, english version, javascript version (web app)
sg.theme('Default1')

#main function of game and layout
def main():
    result = chooseresult()
    COL=5
    ROWS=6
    chars=['','','','','','']
    topRow = 'QWERTYUIOP'
    midRow = 'ASDFGHJKL'
    bottomRow = 'ZXCVBNM'
    layout =[[[sg.Button(chars[i], size=(4, 2), key=(i,j), pad=(0,0), button_color=('white')) for j in range(COL)] for i in range(ROWS)],
                [sg.Txt('Gib das nächste Wort ein:')],
                [sg.In(size=(12,2), key='IN', do_not_clear=False, focus=True)],
                [sg.Button('GO!', bind_return_key=True, button_color=('LightBlue')), sg.Button('Anderes Wort', key=('NW')), sg.Button('Exit')],
                [sg.Text(' ' * 4)] + [sg.Button(c, key=c, size=(2, 1)) for c in topRow] + [sg.Stretch()],
                [sg.Text(' ' * 11)] + [sg.Button(c, key=c, size=(2, 1)) for c in midRow] + [sg.Stretch()],
                [sg.Text(' ' * 18)] + [sg.Button(c, key=c, size=(2, 1)) for c in bottomRow] + [sg.Stretch()]]
    
    win = sg.Window('WannabeWordle', layout, element_justification='c')
    row = 0
    while True:             # Event Loop
        event, values = win.read()
        if event in (None, 'Exit'):
            win.close
            break
        if event == 'NW':
            main()
        if event == 'GO!':
            if len(values['IN']) == 5:    
                userinput = values['IN']
                chars = list(userinput)
                chars = list(map(lambda x: x.upper(), chars))
                for i in range(5):
                    win[row,i].update(chars[i])
                fitchars(win, row,chars,result)
                row +=1
            else: 
                sg.popup('Das Wort muss 5 Buchstaben haben!')
        if event == sg.WIN_CLOSED:
            win.close()
            break

    win.close()

#select a random word as result
def chooseresult():
    result = random.choice(['haben', 'nicht', 'geben', 'sagen', 'durch', 'gegen', 'gehen', 'schon', 'sehen', 'immer', 'unter', 'beide', 'heute', 'damit', 'jetzt', 'dabei', 'Stadt', 'unser', 'sowie', 'unter', 'klein', 'eigen', 'Woche', 'Platz', 'Spiel', 'Seite', 'wegen', 'wenig', 'stark', 'Leben', 'Frage', 'zweit', 'Thema', 'Monat', 'Grund', 'etwas', 'Punkt', 'neben', 'davon', 'sogar', 'leben', 'etwas', 'sechs', 'Meter', 'April', 'wenig', 'zudem', 'dritt', 'legen', 'Staat', 'Preis', 'offen', 'Leute', 'Kreis', 'Musik', 'lange', 'genau', 'knapp', 'Titel', 'Abend', 'Firma', 'trotz', 'Folge', 'daher', 'Vater', 'statt', 'Sache', 'zuvor', 'Hilfe', 'warum', 'Rolle', 'Nacht', 'wenig', 'Mitte', 'daran', 'Autor', 'bauen', 'Markt', 'Blick', 'Recht', 'lesen', 'Krieg', 'Kunst', 'recht', 'Kraft', 'holen', 'laden', 'durch', 'Opfer', 'Karte', 'Kunde', 'Kampf', 'damit', 'aktiv', 'genau', 'sonst', 'rufen', 'Runde', 'gerne', 'Reihe', 'meist', 'Junge', 'Liste', 'Sport', 'Weise', 'Union', 'Druck', 'darin', 'Start', 'teuer', 'bevor', 'Boden', 'Linie', 'Angst', 'viert', 'Liebe', 'darum', 'reden', 'breit', 'Stand', 'wobei', 'weder', 'Hotel', 'links', 'Regel', 'somit', 'Datum', 'Roman', 'Licht', 'genug', 'Motto', 'Sicht', 'stets', 'Natur', 'Alter', 'Serie', 'enden', 'Menge', 'Szene', 'Insel', 'Pause', 'Reise', 'Brief', 'Tisch', 'Macht', 'Osten', 'Farbe', 'Datei', 'Wagen', 'obere', 'Beruf', 'Halle', 'Fahrt', 'Stein', 'Bauer', 'indem', 'einst', 'Sorge', 'Unter', 'Suche', 'Krise', 'Sonne', 'Heute', 'reich', 'Jetzt', 'Figur', 'Armee', 'Leser', 'loben', 'stolz', 'rasch', 'Aktie', 'bitte', 'Tonne', 'Bayer', 'Album', 'Reich', 'Feuer', 'Traum', 'Regie', 'Ihnen', 'Basis', 'Messe', 'Stern', 'Geist', 'unten', 'ernst', 'Waffe', 'ruhig', 'hinzu', 'Kreuz', 'heuer', 'statt', 'heben', 'Blatt', 'dahin', 'vorne', 'Liter', 'Brand', 'Senat', 'Strom', 'Ernst', 'Fluss', 'Feier', 'Galle', 'Zweck', 'Lager', 'Wille', 'enorm', 'Sturm', 'Vogel', 'Coach', 'Pferd', 'Ebene', 'Papst', 'Essen', 'Profi', 'falls', 'Trend', 'essen', 'raten', 'dicht', 'Bezug', 'Motor', 'Marke', 'Linke', 'Klage', 'Zitat', 'Seele', 'Radio', 'Forum', 'Phase', 'Motiv', 'Masse', 'fremd', 'total', 'Regen', 'still', 'indes', 'einig', 'Trotz', 'Summe', 'Zeuge', 'Lehre', 'zumal', 'davor', 'lokal', 'Stoff', 'Mauer', 'Tempo', 'Dauer', 'krank', 'Party', 'Maler', 'allzu', 'Klima', 'Kasse', 'ehren', 'Umbau', 'teils', 'Kader', 'Duell', 'Video', 'malen', 'Beleg', 'Probe', 'Prinz', 'Fisch', 'Krone', 'Blume', 'wagen', 'Front', 'Lokal', 'ideal', 'Weber', 'Laden', 'Schuh', 'Hafen', 'Klang', 'Villa', 'apern', 'Umzug', 'Konto', 'Grand', 'Wende', 'Griff', 'Image', 'Arena', 'Wiese', 'Droge', 'herum', 'Pokal', 'Rente', 'Stock', 'Bitte', 'Schau', 'Orgel', 'Erste', 'Welle', 'Tiefe', 'vorig', 'Stufe', 'typen', 'Brite', 'Hesse', 'exakt', 'Kanal', 'Katze', 'Sturz', 'Serbe', 'mobil', 'Russe', 'hallo', 'leise', 'innen', 'Wesen', 'Wolke', 'einen', 'weise', 'Engel', 'Feind', 'Bruch', 'Brust', 'Zelle', 'Abbau', 'Stuhl', 'voran', 'Fonds', 'Pilot', 'Fuchs', 'Minus', 'quasi', 'Fazit', 'drauf', 'Handy', 'Stamm', 'weich', 'Hobby', 'sanft', 'Areal', 'tagen', 'womit', 'Gunst', 'Block', 'Bombe', 'Drama', 'glatt', 'Humor', 'Zeile', 'Super', 'Islam', 'Chaos', 'Lemma', 'Index', 'Kleid', 'Stolz', 'ruhen', 'Email', 'Faust', 'Pfund', 'Einer', 'Armut', 'Fahne', 'Gramm', 'Orden', 'Blues', 'Heide', 'wieso', 'braun', 'Quote', 'zivil', 'Decke', 'Paket', 'Adler', 'Kugel', 'wohin', 'jagen', 'Milch', 'Tafel', 'These', 'nackt', 'mutig', 'Route', 'Miete', 'flach', 'steil', 'Virus', 'zirka', 'ahnen', 'Bogen', 'Stahl', 'danke', 'Derby', 'heran', 'desto', 'blind', 'Frist', 'Bibel', 'Laune', 'Falle', 'Abzug', 'Beute', 'Tiger', 'Anruf', 'regen', 'Tenor', 'Kette', 'Statt', 'antik', 'Rasen', 'Enkel', 'Moral', 'Gleis', 'Stich', 'Hitze', 'Kurve', 'Onkel', 'Bauch', 'Lache', 'Trick', 'rapid', 'Sorte', 'Remis', 'Treff', 'Faden', 'Lippe', 'Organ', 'Haupt', 'Jacke', 'Schaf', 'Stift', 'Geste', 'Disco', 'nebst', 'Feder', 'Tarif', 'Anbau', 'woher', 'Sound', 'vorab', 'Foyer', 'wehen', 'Glanz', 'extra', 'brach', 'Elite', 'toben', 'Krebs', 'final', 'Nagel', 'wovon', 'royal', 'Jubel', 'Witwe', 'sauer', 'flott', 'Votum', 'Labor', 'Nebel', 'Apfel', 'Gebot', 'Stall', 'extra', 'Gasse', 'Piste', 'Treue', 'Pater', 'First', 'Label', 'drauf', 'Kurde', 'beten', 'Maske', 'alpin', 'Trost', 'Gebet', 'Brett', 'Tante', 'zumal', 'Genre', 'Linde', 'fatal', 'eilen', 'Krimi', 'Kabel', 'Ampel', 'Kopie', 'Fleck', 'Allee', 'Ferne', 'hauen', 'Kerze', 'Panik', 'Logik', 'legal', 'Model', 'Leder', 'Hallo', 'Unmut', 'Nicol', 'wider', 'minus', 'rasen', 'baden', 'Rauch', 'Staub', 'Garde', 'Anzug', 'Sechs', 'Zwang', 'blond', 'Alarm', 'Rasse', 'Wunde', 'Zweig', 'Puppe', 'Busch', 'atmen', 'Altar', 'Segen', 'Eisen', 'Agent', 'Weile', 'Ernte', 'Indiz', 'Panne', 'frech', 'super', 'Ideal', 'Etage', 'Rache', 'Bande', 'Kraut', 'Kiste', 'weben', 'Ruine', 'stumm', 'spitzenus', 'Prosa', 'trist', 'Tower', 'Nonne', 'Wiege', 'Folie', 'Magie', 'kraus', 'herab', 'Mensa', 'Crash', 'eitel', 'Notar', 'grell', 'Inder', 'haken', 'Kehle', 'Promi', 'Sumpf', 'herab', 'Theke', 'steif', 'Birke', 'Enzym', 'Gurke', 'Ferse', 'Blase', 'Unfug', 'Spatz', 'Knall', 'Speck', 'Walze', 'Rille', 'Rumba', 'Humus'])
    #with open("words.txt", "r") as file:
    #    allText = file.read()
    #    words = list(map(str.upper, allText.split()))
    #    result = random.choice(words)
    return result

#search for matching characters between input and result
#mark characters with specific colors
#win or loose message
def fitchars(win, row, chars, result):
    result2 = list(result)
    input = chars
    common = list(set(result2).intersection(input))
    for l in common:
        win[l].update(button_color=('lightgreen'))
    badchars = set(chars) - set(common)
    for b in badchars:
        win[b].update(button_color=('Grey'))
    for let in result2:
        if let in input:
            resind = result2.index(let)
            inpind = input.index(let)
            if  resind == inpind:
                input[resind] = 0
                result2[resind] = 0
                win[row,resind].update(button_color=('green'))
            else:
                if let in input:
                    win[row,inpind].update(button_color=('yellow'))  
    if result2 == input:
        sg.popup('YAY, GEWONNEN!')
        open_window(win)
    if row == 5 and result != chars:
        sg.popup('OH NO! DAS WAR WOHL NIX.')
        open_window(win)

#choose if you want to play another round    
def open_window(win):
    global result
    global row
    layout = [[sg.Text("Und nun?")],
        [sg.Button("Nochmal?", key="new"), sg.Button('Exit')]]
    window = sg.Window("", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit":
            window.close()
            win.close()
            break
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == 'new':
            window.close()
            main()

main()