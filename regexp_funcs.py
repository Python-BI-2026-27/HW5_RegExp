import re

def to_salty_language(text):
    text.lower()
    pattern = r"([аеёиоуыэюя])"
    result = re.sub(pattern, r"\1с\1", text)
    return result

def find_chords(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    pattern = r"\b[A-G]m?\b"
    chords = re.findall(pattern, text)
    uni_chords = set(chords)
    return uni_chords
