![logo](logo.png)
<meta name="google-site-verification" content="MX8kPKC76t4LhECNv81HBUnUSfhRuaku3W7rFjye-AA" />

An (I must admit: ugly, but working!(with some bugs)) clone of the word guessing game [wordle](https://www.powerlanguage.co.uk/wordle/) where you can choose, in which language you want to guess the words (English, German, French, Luxemburgish at the moment. Some more will soon be added). It's a bloody beginner project, therefore it's written in python. Also there is an executable for win, mac and linux. A web app is planned (yeah, i want to learn TypeScript.).

# Get started

For using the little game with python you have to install PySimpleGUI with
```
pip install pysimplegui
```
and start it with the lang folder in the same folder as the python script.

If you choose the one without internal words list (for changing it etc.) make sure, that you put it in the same folder like the main py.

With the executble file (also in releases as standalone), you don't have to install the GUI.

# Rules

You have 6 rounds for guessing the word. Each round the game tells you with
green => That this letter is at the right place
yellow => The letter is in the word, but not at the right place
it stays grey => The letter is not in the word

Also the keyboard graphic tells you, which letters you used, which ones are right and which ones are false (sometimes it's a little bit buggy, will fix that.)

easy! Have fun!

# Please notice
Unfortunately, accents and special characters (latin characters) are reduced to plain characters (à --> a).
Also the word lists are not filtered for strange content. They are frequency lists from wikipedia and national language corpora.

# Footnotes

Game was created by using [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) (Also the keyboard was inspired by the "cookbook")

Wordlists: 
German: [top100000](https://www1.udel.edu/LLL/language/deutsch/top10000.pdf)
English: [kaggle](https://www.kaggle.com/rtatman/english-word-frequency)
Luxembourgish: [6000wierder](https://6000wierder.lu/)
French: [wiktionary](https://en.wiktionary.org/wiki/Wiktionary:French_frequency_lists/1-2000)
Italian: [top10000words](http://www.top10000words.com/Five_letter_Italian_words.html)
Spanish: [rae corpus](http://corpus.rae.es/frec/10000_formas.TXT)
Swedish: [Kelly list](https://spraakbanken.gu.se/en/resources/kelly)


Thanks to my favourite Nebelchen for inspiring me with his awesome excel work! 

Feel free to use this code for project, improvements, make yourself laugh, triggering your code OCD and so on ;-)
