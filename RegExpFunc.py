# RegExp Functions

import os
import re


# salty function
def salty_transformer(text):
    if os.path.isfile(text):
        with open(text, "r", encoding="utf-8") as f:
            text = f.read()
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = []
    for char in text:
        result.append(char)
        if char in vowels:
            s_char = "с"
            result.append(s_char + char.lower())
    return "".join(result)


# extract music chords function
def chord_extract(path):
    chords_symbols = re.compile(
        r"\b[A-G][a-z0-9]{0,2}\b"
    )  # [A-Za-z0-9+]+ для кириллицы
    chords = set()
    with open(path, "r", encoding="utf-8") as file:
        for string in file:
            hits = chords_symbols.findall(string)
            chords.update(hits)
    return chords


# rename files function


def rename_files(dir, pattern, new_pattern, sample_names, to_replace: bool = False):

    for file in os.listdir(dir):
        if re.search(pattern, file):
            new_file = re.sub(pattern, new_pattern, file)

            for (
                old_sample,
                new_sample,
            ) in sample_names.items():
                new_file = new_file.replace(old_sample, new_sample)

            os.replace(os.path.join(dir, file), os.path.join(dir, new_file))
