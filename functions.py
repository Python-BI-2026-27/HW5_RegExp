import os
import re
import shutil


def translate_to_salt(input: str) -> str:
    """Translate from russian to salt language.

    Args:
        input (str): input word / sentence

    Returns:
        str: otput in salt version
    """
    return re.sub(
        r"(?P<vowel>[АЕЁИОУЫЭЮЯаеёиоуыэюя]{1})",
        r"\g<vowel>с\g<vowel>",
        input,
    )


def get_chords(lyrics_for_parse: str) -> set[str]:
    """Get all uniqe chords from songs lyrics.

    Args:
        lyrics_for_parse (str): path to file

    Returns:
        set[str]: All parsed chords in tuple
    """
    chord_pattern = r"(?:[CDEFGAB]#?(?:maj|m|sus|add|aug|dim)?[24579]?)"
    with open(lyrics_for_parse) as lyrics:
        chords = set(
            re.findall(
                pattern=chord_pattern,
                string=lyrics.read(),
            ),
        )
    return chords


def rename_files(
    dir: str,
    pattern: str | None = None,
    new_pattern: str | None = None,
    sample_names: dict[str, str] | None = None,
    to_replase: bool = False,
) -> None:
    """Rename all files in directory by pattern.

    Args:
        dir (str): path to directory with '/'
        pattern (str): what need to replace
        new_pattern (str): what need to insert
        sample_names (dict[str,str]): dict with replace rules
        to_replase (bool): flag to replace old names by new ones
    """
    files_for_rename = os.listdir(dir)
    for old_name in files_for_rename:
        if pattern and new_pattern:
            new_name = re.sub(
                pattern,
                new_pattern,
                old_name,
            )

        if sample_names:
            for target_pattern, sample_pattern in sample_names.items():
                if target_pattern in old_name:
                    if new_name:
                        new_name = re.sub(
                            target_pattern,
                            sample_pattern,
                            new_name,
                        )
                    else:
                        new_name = re.sub(
                            target_pattern,
                            sample_pattern,
                            old_name,
                        )

        change_in_path = (dir + old_name, dir + new_name)
        if to_replase:
            print(*change_in_path, sep="->")
            os.rename(*change_in_path)
        elif old_name is not new_name:
            shutil.copy2(*change_in_path)
        else:
            print(f"{new_name} - уже переименован")
