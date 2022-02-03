import PySimpleGUI as sg
import random
from collections import Counter 

sg.theme('Default1')

with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str.upper, allText.split()))
    result = random.choice(words)
    print (result)

def fitchars(row, chars, result):
    result2 = result
    dict1 = Counter(str(chars))
    dict2 = Counter(result2)
    commonDict = dict1 & dict2
    commonChars = list(commonDict.elements())
    indlist = []
    if not len(commonChars) == 0:
        for letter in commonChars:
            letind = result2.index(letter)
            indlist.append(letind)
            result2 = result[:letind] + '0' + result2[letind+1:]
            for ind in indlist:
                win[row,ind].update(button_color=('green'))


COL=5
ROW=6
chars=['','','','','','']
layout =[[[sg.Button(chars[i], size=(4, 2), key=(i,j), pad=(0,0)) for j in range(COL)] for i in range(ROW)],
            [sg.Txt('Gib das nächste Wort ein:')],
            [sg.In(size=(12,2), key='IN')],
            [sg.Button('GO!'), sg.Button('Exit')]]

win = sg.Window('WannabeWordle', layout)

while True:             # Event Loop
    event, values = win.read()
    if event in (None, 'Exit'):
        break
    if event == 'GO!':
        if len(values['IN']) == 5:    
            userinput = values['IN']
            chars = list(userinput)
            chars = list(map(lambda x: x.upper(), chars))
            row = 0
            for i in range(5):
                win[row,i].update(chars[i])
            fitchars(row,chars, result)
        else: 
            sg.popup('Das Wort muss 5 Buchstaben haben!')
        
win.close()