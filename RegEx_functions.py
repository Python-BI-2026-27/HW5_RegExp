import re

#Salty language translator
def salty_lang(string):
    for letter in 'аоуеыэёяиюАОУЕЫЭЁЯИЮ':
        string = re.sub(letter, letter + 'c' + letter.lower(), string)
    return(string)