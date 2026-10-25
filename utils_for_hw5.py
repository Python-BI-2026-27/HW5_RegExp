import os
import re


def tranfer_to_salty(text):
    pattern = r"([аеёяиуыоэюАЕЁЯИУЫОЮЭ])"
    result = re.sub(pattern=pattern, repl=r"\1с\1", string=text)
    return result


def tranfer_to_chrods(path):
    with open(path) as file:
        text = file.read()
    pattern = r"[A-Z]\w*"
    result = set(re.findall(pattern=pattern, string=text))
    return result


def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    renamed = {}
    files = os.listdir(dir)
    for f in files:
        new_name = f
        if new_pattern:
            new_name = re.sub(pattern, new_pattern, new_name)
        if sample_names:
            for old, new in sample_names.items():
                new_name = re.sub(old, new, new_name)
        if new_name == f:
            continue
        if to_replace:
            os.rename(os.path.join(dir, f), os.path.join(dir, new_name))
        else:
            with (
                open(os.path.join(dir, f), "rb") as src,
                open(os.path.join(dir, new_name), "wb") as dst,
            ):
                dst.write(src.read())
        renamed[f] = new_name
    return renamed
