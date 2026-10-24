import os
import re


def to_salted_language(text: str) -> str:
    """After each vowel (ru), a specific consonant—for example, "c"(ru)—is added, followed by that same vowel once again."""
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = []

    for char in text:
        result.append(char)
        if char in vowels:
            result.append("c" + char.lower())

    return "".join(result)


def extract_chords(file_path: str) -> set[str]:
    """Exctract found chords from a file with song's lyrics and chords."""
    chord_pattern = re.compile(
        r"\b[A-G][#b]?(?:m|maj|min|sus|dim|aug|\d)*(?:/[A-G][#b]?)?\b"
    )  # ¯\_(ツ)_/¯ what do we play on?

    chords = set()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            found_chords = chord_pattern.findall(line)
            chords.update(found_chords)

    return chords


def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str | None = None,
    sample_names: dict[str, str] | None = None,
    to_replace: bool = False,
) -> None:
    """Rename files by pattern or dictionary or by both consequence"""
    for filename in os.listdir(dir):
        # Filter by pattren
        if pattern not in filename:
            continue

        old_path = os.path.join(dir, filename)
        new_name = filename

        # Replace by pattern
        if new_pattern is not None:
            new_name = new_name.replace(pattern, new_pattern)

        # Replace by dict
        if sample_names:
            for old_sample, rep_sample in sample_names.items():
                if old_sample in new_name:
                    new_name = new_name.replace(old_sample, rep_sample)

        # If no name change, skip
        if new_name == filename:
            continue

        new_path = os.path.join(dir, new_name)

        if to_replace:
            os.replace(old_path, new_path)
        else:
            with open(old_path, "rb") as src, open(new_path, "wb") as dst:
                dst.write(src.read())
