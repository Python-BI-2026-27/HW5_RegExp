import re
import os

def solenyi_translation(string):
    pattern = r'([аеёиоуыэюяАЕЁИОУЫЭЮЯ])'
    replacement = r'\1c\1'
    return re.sub(pattern,replacement,string)

def chords_extraction(file):
    with open (file, mode='r') as f:
        text = f.read()

        pattern = r"[A-G]m?"
        chords = set(re.findall(pattern,text))
        return chords

def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    if sample_names is None:
        sample_names = {}

    all_files = os.listdir(dir)

    for filename in all_files:

        old_path = os.path.join(dir, filename)

        if re.search(pattern, filename) is None:
            continue

        new_name = filename

        if new_pattern is not None:
            new_name = re.sub(pattern, new_pattern, new_name)

        for old_sample, new_sample in sample_names.items():
            new_name = new_name.replace(old_sample, new_sample)

        new_path = os.path.join(dir, new_name)

        if new_path == old_path:
            continue

        if to_replace:
            os.rename(old_path, new_path)
        else:
            with open(old_path, "r") as input:
                with open(new_path, "w") as output:
                    output.write(input.read())


