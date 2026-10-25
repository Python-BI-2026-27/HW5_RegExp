import os
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


def rename_files(dir, pattern, sample_names, new_pattern=None, to_replace=False):
    files = os.listdir(dir)
    for file in files:
        if not os.path.isfile(os.path.join(dir, file)):
            continue
        if new_pattern is not None:
            new_file = re.sub(pattern, new_pattern, file)
            with (
                open(os.path.join(dir, file)) as source,
                open(os.path.join(dir, new_file), "w") as result,
            ):
                result.write(source.read())
            if to_replace:
                os.remove(os.path.join(dir, file))
        else:
            new_file = file
        for sample_name, replacement in sample_names.items():
            final_file = re.sub(sample_name, replacement, new_file)
            if final_file == new_file:
                continue
            with (
                open(os.path.join(dir, new_file)) as source,
                open(os.path.join(dir, final_file), "w") as result,
            ):
                result.write(source.read())
        if to_replace:
            os.remove(os.path.join(dir, new_file))
