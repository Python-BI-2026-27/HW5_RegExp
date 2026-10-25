import re
import os
import shutil


def translate_to_salty_language(russian: str) -> str:
    """
    Translation of the Russian phrase or word into the salty language
    (Add the letter “c” after the vowel, followed by the same vowel)

    Arguments:
    russian: str: a phrase in Russian

    Returns:
    str: a phrase in salty language
    """
    pattern = r"([ауоыэяюёие])"
    replacement = r"\g<1>с\g<1>"
    salty = re.sub(pattern, replacement, russian, flags=re.I)
    return salty


def get_chords_from_song_text(input_song_file: str) -> set:
    """
    Find chords in the song's text

    Arguments:
    input_song_file: str: the path to the file

    Returns:
    set: a set of chords from input_song_file
    """
    with open(input_song_file, encoding="utf-8") as song_file:
        song_text = song_file.read()
        pattern = r"\b[ABCDEFGH]\d?#?(?:sus|b|maj|m)?(?:/[ABCDEFGH])?(?:\d{1,2})?\b#?"  # Извините, раньше играла на гитаре, решила побаловаться-поприкаловаться
        chords = set(re.findall(pattern, song_text))
        return chords


def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str | None = None,
    sample_names: dict | None = None,
    to_replace: bool = False,
) -> None:
    """
    Renames the files in the folder
    and saves the renamed files with a new name, deleting the old ones
    or creating copies with the new name

    Arguments:
    dir: str: path to directory
    pattern: str: replacement string for files selection and to be replaced with a new pattern
    new_pattern: str| None = None: replacement string for renaming a file (optional)
    sample_names: dict | None = None: a dictionary with renaming rules (optional)
    to_replace: bool = False: True - rename file and delete old, False - copy file with a new name
    """
    for name in os.listdir(dir):
        path_file = os.path.join(dir, name)
        if os.path.isfile(path_file):
            match_with_pattern = re.search(pattern, name)
            if match_with_pattern is not None:
                if new_pattern is None:
                    new_name = name
                else:
                    new_name = re.sub(pattern, new_pattern, name)
                if sample_names is not None:
                    for key, value in sample_names.items():
                        new_name = new_name.replace(key, value)
                if new_name != name:
                    new_path_file = os.path.join(dir, new_name)
                    if to_replace == True:
                        os.rename(path_file, new_path_file)
                    else:
                        shutil.copy(path_file, new_path_file)
