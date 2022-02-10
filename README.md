![logo](logo.png)

An (I must admit: ugly, but working!) clone of the word guessing game [wordle](https://www.powerlanguage.co.uk/wordle/) where you can choose, in which language you want to guess the words (English, German, French, Luxemburgish, Spanish, Italian, Swedish, Dutch, Portuguese, Norwegian, Finnish, Danish and Latin). It's a bloody beginner project, therefore it's written in python. Also there is an executable for win, mac and linux. A web app is planned (yeah, i want to learn TypeScript.).

# Get started

For using the little game with python you have to install PySimpleGUI with
```
pip install pysimplegui
```
and start it with the lang folder in the same folder as the python script.

If you choose the one without internal words list (for changing it etc.) make sure, that you put it in the same folder like the main py.

With the executble file (also in releases as standalone), you don't have to install the GUI. Sometimes Windows Defender or other Antimalware scanners will show a warning, when you try to execute the file. It's because of the base64 encrypted images in the game. I garantuee that the software is free from malware. 

# Rules

You have 6 rounds for guessing the word. Each round the game tells you with
green => That this letter is at the right place
yellow => The letter is in the word, but not at the right place
it stays grey => The letter is not in the word

Also the keyboard graphic tells you, which letters you used, which ones are right and which ones are false (sometimes it's a little bit buggy, will fix that.)

easy! Have fun!

# Please notice
Unfortunately, accents and special characters (latin characters) are reduced to plain characters (à --> a).
Also the word lists are just not much filtered for strange or explicit content, sometimes names. They are mostly frequency lists from wikipedia, open subtitles and national language corpora.

# Footnotes

Game was created by using [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) (Also the keyboard was inspired by the "cookbook")

Wordlists: 
Just original fragments, not the whole lists and under common licence:
German, English, Italian: [Github](https://github.com/hermitdave/FrequencyWords),
Luxembourgish: [lod](https://data.public.lu/en/datasets/letzebuerger-online-dictionnaire-raw-data/),
French: [wiktionary](https://en.wiktionary.org/wiki/Wiktionary:French_frequency_lists/1-2000),
Spanish: [rae corpus](http://corpus.rae.es/frec/10000_formas.TXT),
Swedish: [Kelly list](https://spraakbanken.gu.se/en/resources/kelly),
Dutch: [wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Dutch_wordlist),
Portuguese: [wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Portuguese_wordlist),
Norwegian: [wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Norwegian),
Finnish: [csc.fi](https://web.archive.org/web/20140807150829/http://www.csc.fi/tutkimus/alat/kielitiede/taajuussanasto-B9996/view),
Danish: [dsl corpus](https://korpus.dsl.dk/resources/licences/dsl-open.html#list),
Latin: [latin 202](https://documents.kenyon.edu/classics/current/2099.wordlistforlatn202alphabetical.pdf)


Thanks to my favourite Nebelchen for inspiring me with his awesome excel work! 

Feel free to use this code for project, improvements, make yourself laugh, triggering your code OCD and so on ;-)
