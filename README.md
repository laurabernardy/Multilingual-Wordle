![logo](logo.png)

An (I must admit: ugly, but working!) clone of the word guessing game [wordle](https://www.powerlanguage.co.uk/wordle/) in german language (WannabeWordle == "Möchtegern Wordle"). It's a bloody beginner project, therefore it's written in python. Also there is an executable for win, mac and linux. An english or multilingual version and a web app is planned (yeah, i want to learn Typescript.).

# Get started

For using the little game with python you have to install PySimpleGUI with
```
pip install pysimplegui
```
If you choose the one without internal words list (for changing it etc.) make sure, that you put it in the same folder like the main py.

With the executble file (also in releases as standalone), you don't have to install the GUI.

# Rules

You have 6 rounds for guessing the word. Each round the game tells you with
green => That this letter is at the right place
yellow => The letter is in the word, but not at the right place
it stays grey => The letter is not in the word

Also the keyboard graphic tells you, which letters you used, which ones are right and which ones are false (sometimes it's a little bit buggy, will fix that.)

easy! Have fun!

# Footnotes

Game was created by using [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) (Also the keyboard was inspired by the "cookbook")

Thanks to my favourite Nebelchen for inspiring me with his awesome excel work! 

Feel free to use this code for project, improvements, make yourself laugh, triggering your code OCD and so on ;-)
