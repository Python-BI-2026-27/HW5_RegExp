import re

#Salty language translator
def salty_lang(string):
    for letter in 'аоуеыэёяиюАОУЕЫЭЁЯИЮ':
        string = re.sub(letter, letter + 'c' + letter.lower(), string)
    return(string)

#Chords extractor
def chords_extractor(file):
    with open('./data/song.txt') as file:
        pattern = r'[A-Z]{1}[^\s]*'
        all_chords = set()
        for line in file:
            chords = re.findall(pattern, line)
            all_chords.update(chords)
    return all_chords