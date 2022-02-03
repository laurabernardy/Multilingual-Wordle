import PySimpleGUI as sg
import random
import re
from collections import Counter 

sg.theme('Default1')

with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str.upper, allText.split()))
    result = random.choice(words)
    print (result)

def special_match(strg, search=re.compile(r'[^a-z]').search):
         return not bool(search(strg))

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
                win[row,resind].update(button_color=('green'))
            else:
                if let in input:
                    win[row,inpind].update(button_color=('yellow'))


            
             
    #dict1 = Counter(str(chars))
    #dict2 = Counter(result2)
    #commonDict = dict1 & dict2
    #print (commonDict)
    #commonChars = list(commonDict.elements())
    #print(commonChars)
    #indlist = []
    #if not len(commonChars) == 0:
    #    for letter in commonChars:
    #        if letter in result2:
    #            letind = result2.index(letter)
    #            inpind = chars.index(letter)
    #            indlist.append(letind)
    #            for i in indlist:
    #                print(i)
    #                if i == inpind:
    #                    result2 = result2[:inpind] + '0' + result2[inpind+1:]
    #                    win[row,i].update(button_color=('green'))
    #                else:
    #                    if letter in result2:
    #                        result2 = result2[:inpind] + '0' + result2[inpind+1:]
    #                        print (result2)
    #                        win[row,i].update(button_color=('yellow'))

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