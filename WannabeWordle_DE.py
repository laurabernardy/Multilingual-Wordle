import PySimpleGUI as sg
import random

#todo: Design stuff, not in words list, multilingual version, javascript version (web app)
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


#select a random word as result from external list
def chooseresult():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str.upper, allText.split()))
        result = random.choice(words)
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