import re
from pathlib import Path

def turn_txt_into_pig_latin(input_file):
    with open(input_file) as txt:
        lines = []
        for line in txt:
            translation = re.sub(r"([АЕЁИОУЫЭЮЯаеёиоуыэюя])", r"\1с\1", line)
            lines.append(translation)
        result = ''.join(lines)
    return result


def get_song_chords(input_file):
    with open(input_file) as song:
        chords = set()
        for line in song:
            result = re.findall(r"\b([CDEFGAHB][#b]?m?(?:dim|sus|maj)?[1-9]?(?:/[CDEFGAHB][#b]?)?)(?:\s|$)", line)
            chords.update(result)
    return chords


def rename_files(dir, pattern, new_pattern = None, sample_names = None, to_replace = False):
    for file in Path(dir).iterdir():
        matches = re.search(pattern = pattern, string = file.name)
        if matches is None:
            continue
        new_name = file.name
        if new_pattern is not None:
            new_name = re.sub(pattern, new_pattern, new_name)
        if sample_names is not None:
            for key, value in sample_names.items():
                new_name = new_name.replace(key, value)
        p = file.parent/new_name
        if to_replace:
            file.rename(p)
        else:
            file.copy(p)