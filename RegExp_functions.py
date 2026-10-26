import re

def convert_to_salted(text: str) -> str:
    """
    Converts text from Russian into so called salted language

    Arguments:
        text(str): path to the input file

    Returns:
        str: converted text
    """
    vowels = r"[аеёиоуыэюяАЕЁИОУЭЮЯ]"

    def replace_vowel(match):
        vowel = match.group()
        return(vowel + 'с' + vowel)
    return(re.sub(vowels, replace_vowel, text))

def find_chords(song: str) -> set:
    """
    Finds all chords in the song text file

    Arguments:
        song(str): path to the song text file

    Returns:
        set: a set of unique chords found in the file
    """
    chords = r"\b[A-Z][a-z]*\b"
    
    with open(song, encoding="utf-8") as file:
        text = file.read()
        result = re.findall(chords, text) 
        return set(result)
