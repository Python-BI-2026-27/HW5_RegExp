import re

def make_text_salty(text):
    """Change language to salty language"""
    pattern = r'([аеёиоуыэюяАЕЁИОУЫЭЮЯ])'
    result = re.sub(pattern, r'\1с\1', text)
    return result

def get_chords(path):
    """Get chords from Russian language text file"""
    chords = set()

    with open(path, encoding='utf-8') as file:
        for line in file:
            if not re.search(r'[а-яА-ЯёЁ]', line):
                found = re.findall(r'[A-G][#b]?m?', line)
                chords.update(found)

    return chords