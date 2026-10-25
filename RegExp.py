import re
from pathlib import Path
import shutil

def rus2salt(text):
    pattern = r'[АЕЁИОУЫЭЮЯаеёиоуыэюя]'
    result = ''
    for letter in text:
        if re.match(pattern, letter):
            if letter.isupper():
                result += letter + 'C' + letter
            else:
                result += letter + 'c' + letter
        else:
            result += letter
    print(result)
    return result

def get_chords(file_path):
    with open(file_path, mode = 'r') as f:
        text = f.read()

    pattern = (
        r'(?<![A-Za-z])'
        r'[A-H](?:#|b)?'
        r'(?:maj|min|m|dim|aug|sus\d*)?'
        r'\d*(?:/[A-H](?:#|b)?)?'
        r'(?![A-Za-z])'
    )

    chords = set(re.findall(pattern, text))
    print(chords)

    return chords

def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    directory = Path(dir)

    for file in directory.iterdir():
        if re.search(pattern, file.name):
            if new_pattern is not None:
                new_name = re.sub(pattern, new_pattern, file.name)
            else:
                new_name = file.name

            if sample_names is not None:
                for old_name, new_sample_name in sample_names.items():
                    new_name = new_name.replace(old_name, new_sample_name)

            if new_name != file.name:
                new_path = directory / new_name

                if to_replace:
                    file.rename(new_path)
                else:
                    shutil.copy2(file, new_path)

    