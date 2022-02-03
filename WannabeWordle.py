import PySimpleGUI as sg
import random

#todo: keyboard, englisch, design, package/standalone
sg.theme('Default1')

def chooseresult():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str.upper, allText.split()))
        result = random.choice(words)
    return result

def fitchars(row, chars, result):
    result2 = list(result)
    input = chars
    for let in result2:
        if let in input:
            print(input)
            resind = result2.index(let)
            inpind = input.index(let)
            print(resind)
            print(inpind)
            if  resind == inpind:
                input[resind] = 0
                result2[resind] = 0
                win[row,resind].update(button_color=('green'))
            else:
                if let in input:
                    win[row,inpind].update(button_color=('yellow'))  
    if result2 == input:
        sg.popup('YAY, GEWONNEN!')
        open_window(COL, ROWS)

def open_window(COL=5, ROWS=6):
    global result
    global row
    global win
    layout = [[sg.Text("Und nun?")],
        [sg.Button("Nochmal?", key="new"), sg.Button('Exit')]]
    window = sg.Window("", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            win.close()
            break
        if event == 'new':
            row = -1
            chars=['','','','','','']
            result = chooseresult()
            for i in range(COL):
                for r in range(ROWS):
                    win[r,i].update(button_color=('white'))
                    win[r,i].update(chars[i])
                    window.close()
             
result = chooseresult()
print(result)
COL=5
ROWS=6
chars=['','','','','','']
layout =[[[sg.Button(chars[i], size=(4, 2), key=(i,j), pad=(0,0), button_color=('white')) for j in range(COL)] for i in range(ROWS)],
            [sg.Txt('Gib das nächste Wort ein:')],
            [sg.In(size=(12,2), key='IN', do_not_clear=False)],
            [sg.Button('GO!', bind_return_key=True), sg.Button('Exit')]]
win = sg.Window('WannabeWordle', layout)
row = 0
while True:             # Event Loop
    event, values = win.read()
    if event in (None, 'Exit'):
        break
    if event == 'GO!':
        if len(values['IN']) == 5:    
            userinput = values['IN']
            chars = list(userinput)
            chars = list(map(lambda x: x.upper(), chars))
            for i in range(5):
                win[row,i].update(chars[i])
            fitchars(row,chars,result)
            row +=1
        else: 
            sg.popup('Das Wort muss 5 Buchstaben haben!')
    
win.close()