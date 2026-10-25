import re


def salt_language(text):
    for i in "аяоиеёуыэю":
        text = re.sub(i, i + "с" + i, text)
        text = re.sub(i.upper(), i.upper() + "с" + i, text)
    return text
