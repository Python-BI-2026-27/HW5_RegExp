import re


def salt_lang_translate(text):
    pattern = r"([АаЕеёЁИиОоУуЫыЭэЮюЯя])"
    salt_text = re.sub(pattern, r"\1с\1", text)
    return salt_text


def chord_collect(path):
    pattern = r"[A-G][\w#/]*"
    with open(path, encoding="utf-8") as song:
        chords = set(re.findall(pattern, song.read()))
    return chords
