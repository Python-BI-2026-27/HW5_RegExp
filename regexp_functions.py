import re
import os
import shutil


def salty_language(text):
    pattern = r'([аоуэияеыёюАОУЭИЯЕЫЁЮ])'
    result = re.sub(pattern, r'\1с\1', text)
    return result

def find_chords(file_path):
    pattern = r'\b[A-G]m?\b'
    with open(file_path, encoding='utf-8') as f:
        text = f.read()

    result = re.findall(pattern, text)
    return set(result)


def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    for filename in os.listdir(dir):
        if re.search(pattern, filename):
            new_name = filename

            if new_pattern is not None:
                new_name = re.sub(pattern, new_pattern, new_name)

            if sample_names is not None:
                for old_sample in sample_names:
                    new_name = new_name.replace(old_sample, sample_names[old_sample])

            if new_name != filename:
                old_path = os.path.join(dir, filename)
                new_path = os.path.join(dir, new_name)

                if not os.path.exists(new_path):
                    if to_replace:
                        os.rename(old_path, new_path)
                    else:
                        shutil.copy(old_path, new_path)
