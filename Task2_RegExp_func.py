import re
import shutil
import os
# Функцию которая осуществляет перевод с русского на "солёный язык" (Wiki).
def to_sour(text):
    pattern = '[АаЕеЁёИОоУуЫыЭэЮюЯя]'
    return re.sub(pattern, r"\g<0>с\g<0>", text)

#Функция которая принимает на вход путь до файла с текстом 
# + аккордами песни и возвращает имеющиеся там аккорды (set).
#  Файл пример song.txt приложен в папке data.
#  Достаточно чтобы работало только с русскими песнями как в примере.
def chords(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as song:
        text = song.read()
        pattern = r'[A-Za-z^{x]{1,}'
        chords = re.findall(pattern, text)
        chords = set(chords)
        chords.remove('x')
        print(chords)

def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str,
    sample_names: dict,
    to_replace: bool):
    
    dirfiles = os.listdir(dir)
    new_paths = []
    files = [file for file in dirfiles if re.findall(pattern, file)]

    if new_pattern:
        for file in files:
            new_path = os.path.join(dir, re.sub(pattern, new_pattern, file))
            new_paths.append(new_path)

            if to_replace:
                os.rename(
                    os.path.join(dir,file),
                    new_path
                    )
            else:
                shutil.copy(
                    os.path.join(dir,file),
                    new_path
                    )


    for key, value in sample_names.items():
        files = [file for file in dirfiles if re.findall(key, file)]
        for file in files:
            new_path = os.path.join(dir, re.sub(key, value, file))
            
            if to_replace:
                os.rename(
                    os.path.join(dir,file),
                    new_path
                    )
            else:
                shutil.copy(
                    os.path.join(dir,file),
                    new_path
                    )
    

