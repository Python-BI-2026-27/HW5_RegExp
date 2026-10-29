
import re
import os
import shutil


def to_salty_language(text: str):
    
    '''
    Translates Russian text into salty language
    '''

    vowels = "аеёиоуыэюя"
    result = ""

    for char in text:
        if char.lower() in vowels:
            result += char + "с" + char.lower()
        else:
            result += char

    return result


def find_chords(file_path: str):
    
    '''
    Returns chords from the file with a song
    
    Chord syntax: (simplified from google)
    "[A-G]" - Root note (A, B, C...)
    "[#b]?" - Optional sharp (#) or flat (b)
    "m?" - Optional 'm' for minor
    "\d?" - Optional extension number (7, 9...)
    "(?:/...)?" - Optional slash bass note (/E)
    '''

    with open(file_path, encoding = "utf-8") as file:
        text = file.read()

    pattern = r'\b[A-G][#b]?m?\d?(?:/[A-G][#b]?)?\b'
    
    result = set(re.findall(pattern, text))

    return result


def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str | None = None,
    sample_names: dict[str, str] | None = None,
    to_replace: bool = False):
    
    '''
    Changes names or copies files according to rules
    '''

    for filename in os.listdir(dir):
        source = os.path.join(dir, filename)

        if not os.path.isfile(source) or not re.search(pattern, filename):
            continue

        new_name = filename

        if new_pattern is not None:
            new_name = re.sub(pattern, new_pattern, new_name)

        if sample_names is not None:
            for old, new in sample_names.items():
                new_name = new_name.replace(old, new)

        if new_name == filename:
            continue

        target = os.path.join(dir, new_name)


        if to_replace:
            os.rename(source, target)
        else:
            shutil.copy2(source, target)
