import re


def translate_to_salty(text: str) -> str:
    """Переводит русский текст на солёный"""

    lower_bukva = r"([аеёиоуыэюя])"  #  Паттерны для поиска гласных
    upper_bukva = r"([АЕЁИОУЫЭЮЯ])"

    # замена для строчных букв
    text = re.sub(lower_bukva, r"\1с\1", text)

    # замену для заглавных букв
    def sub_upper(match):
        v = match.group(1)
        return v + "С" + v.lower()

    return re.sub(upper_bukva, sub_upper, text)
