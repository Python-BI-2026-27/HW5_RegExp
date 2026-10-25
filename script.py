import re
import os

def salt_language(string):
    """
    Перевод с русского на "соленый язык". На вход подается строка,возвращается строка.
    """
    pattern = r'([аеёиоуыэюяАЕЁИОУЫЭЮЯ])'
    result = re.sub(pattern, r'\1с\1', string)
    return result


def music(filepath):
    """
    Функция выводит аккорды (без повторений), использующиеся в русскоязычной песни
    """
    pattern = r"\b[A-G][#b]?m?\d*\b"
    with open(filepath) as f:
        result = set(re.findall(pattern, f.read()))
        return result

def rename_files(dir,pattern,new_pattern = None,sample_names = None,to_replace = False):
    """
        Переименофание файлов с перезаписью/копированием (аргумен to_replace)

        dir: папка с целевыми файлами
        pattern: регулярное выражение для поиска файлов, которые необходимо переименовать
        new_pattern: паттерн переименования. По умолчанию = None
        param sample_names: словарь {'что меняем': 'на что меняем'}. По умолчанию = None
        to_replace: True — переименовать, False — создание копии с новым именем (по умолчанию)
        """
    for filename in os.listdir(dir):
        old_path = os.path.join(dir, filename)
        if not os.path.isfile(old_path):
            continue
        if not re.search(pattern, filename):
            continue
        new_filename = filename
        if new_pattern is not None:
            new_filename = re.sub(pattern, new_pattern, new_filename)
        if sample_names is not None:
            for old_name, new_name in sample_names.items():
                new_filename = new_filename.replace(old_name, new_name)
        if new_filename == filename:
            continue

        new_path = os.path.join(dir, new_filename)
        if os.path.exists(new_path):
            continue


        if to_replace == True:
            os.rename(old_path, new_path)
        elif to_replace == False:
            with open (old_path, 'rb') as f_in, open(new_path, 'wb') as f_out:
                    f_out.write(f_in.read())



