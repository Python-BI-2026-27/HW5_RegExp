import re
import os
import shutil


# соленый язык
def salty_language(text):
    pattern = r"[аеёиоуыэюяАЕЁИОУЫЭЮЯ]"

    def replace(match):
        vowel = match.group()
        return vowel + "с" + vowel.lower()

    return re.sub(pattern, replace, text)


# поиск аккордов
def get_chords(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r"\b[A-G](?:#|b)?(?:m|7|m7)?\b"

    chords = re.findall(pattern, text)

    return set(chords)


# переименование файлов
def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):

    for filename in os.listdir(dir):
        if not re.search(pattern, filename):
            continue

        new_name = filename

        if new_pattern is not None:
            new_name = re.sub(pattern, new_pattern, new_name)

        if sample_names is not None:
            for old, new in sample_names.items():
                new_name = new_name.replace(old, new, 1)

        old_path = os.path.join(dir, filename)
        new_path = os.path.join(dir, new_name)

        if old_path == new_path:
            continue

        if to_replace:
            os.rename(old_path, new_path)
        else:
            shutil.copy2(old_path, new_path)
