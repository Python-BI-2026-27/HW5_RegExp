import re


def translate_to_salty_language(text: str) -> str:
    """Translate Russian into salty language.
    
    Args:
        text: Russian text to translate.

    Returns:
        The text in salty language.
    """
    pattern = r"([уеыаоэёяиюУЕЫАОЭЁЯИЮ])"
    # Нашла в документации как менять то, что совпало (lower в lambda)
    return re.sub(pattern, lambda m: m.group(1) + "с" + m.group(1).lower(), text)


def get_chords(file_path: str) -> set:
    """Return the set of chords found in a song file.

    A chord is a capital letter A-H, optionally followed by m
    and optionally by digit. The chord must be a whole word.
    """
    pattern = r"\b[A-H]m?\d?\b"
    with open(file_path, "r") as file:
        text = file.read()
    return set(re.findall(pattern, text))


def test_fun_translate_to_salty_language():
    text = "У попа была собака, он её любил. Она съела кусок мяса, он её убил."
    salty_text = translate_to_salty_language(text)
    ref_salty_text = (
        "Усу посопаса бысыласа сособасакаса, осон есеёсё люсюбисил. "
        "Осонаса съеселаса кусусосок мясясаса, осон есеёсё усубисил."
    )
    if ref_salty_text == salty_text:
        print("All matched")
    else:
        print("Let's start again (Misha)...")
    print("Our : ", salty_text)
    print("Reference: ", ref_salty_text)


def test_fun_get_chords():
    file_path = "data/song.txt"
    chords = get_chords(file_path)
    ref_chords = {"Am", "C", "Dm", "E", "F", "G"}
    if chords == ref_chords:
        print("All matched")
    else:
        print("Let's start again (Misha)...")
    print("Our : ", chords)
    print("Reference: ", ref_chords)


# Этот код не выполняется при import, но был удобнее для проверок
if __name__ == "__main__":
    test_fun_translate_to_salty_language()
    test_fun_get_chords()
    