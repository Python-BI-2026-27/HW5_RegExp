"""
A set of functions for practicing regular expressions.
"""

import re
import os
import shutil


def salt_transl(text: str):
    """Translate russian text to salt language"""
    return re.sub(r"([АЕЁИОУЫЭЮЯаеёиоуыэюя])", r"\1с\1", text)


def chord_extractor(song: str):
    """
    A function that takes the path to a file containing song lyrics
    and chords, and returns the chords found in the file.
    Only works with Russian-language lyrics.
    """
    with open(song, mode="r", encoding="utf-8") as song_file:
        text = song_file.read()
        pattern = r"([A-H][^ \n]*)"
        chords = set()
        chords.update(re.findall(pattern=pattern, string=text))
        return chords


def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str = None,
    sample_names: dict = None,
    to_replace: bool = False,
):
    """Rename or copy files using patterns and sample names."""

    # Read filenames
    read_file_names = os.listdir(dir)
    sampled_file_names = []
    new_file_names = []

    # Find filenames that match the pattern
    for name in read_file_names:
        if re.search(pattern, name):
            sampled_file_names.append(name)

    for name in sampled_file_names:
        new_file_name = name

        # Replace according to the new pattern
        if new_pattern is not None:
            new_file_name = re.sub(pattern, new_pattern, new_file_name)

        # Replace according to the dictionary
        if sample_names is not None:
            for old_name, new_name in sample_names.items():
                if new_file_name.startswith(old_name + "_"):
                    new_file_name = new_file_name.replace(
                        old_name + "_", new_name + "_", 1
                    )
                    break

        new_file_names.append(new_file_name)

    for i in range(len(sampled_file_names)):
        old_name = sampled_file_names[i]
        new_name = new_file_names[i]
        old_path = os.path.join(dir, old_name)
        new_path = os.path.join(dir, new_name)

        # Skip files if names have not changed
        if old_path == new_path:
            continue

        if to_replace:
            os.rename(old_path, new_path)
        else:
            shutil.copy2(old_path, new_path)
