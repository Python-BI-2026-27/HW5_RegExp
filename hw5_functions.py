import os
import re

# солёный язык
def salty_language(text):
    # функция для замены, после гласной ставим с и ее же еще раз
    def add_sol(gl):
        bukva = gl.group(0)
        return bukva + 'с' + bukva.lower()

    result = re.sub(r'[аеёиоуыэюяАЕЁИОУЫЭЮЯ]', add_sol, text)
    return result
# достаем аккорды из файла с песней
def get_chords(path):
    file = open(path, encoding='utf-8')
    song = file.read()
    file.close()
    # в русской песне латинские буквы только в акордах вроде
    akkords = re.findall(r'[A-H]#?m?7?', song)
    return set(akkords)

# переименовка файлов
def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    files = os.listdir(dir)
    for fname in files:
        # пропускаем файлы которые не подходят под паттерн
        if re.search(pattern, fname) is None:
            continue
        new_fname = fname
        # меняем по паттерну если он есть
        if new_pattern != None:
            new_fname = re.sub(pattern, new_pattern, new_fname)
        # меняем названия образцов по словарю
        if sample_names != None:
            for old_smpl, new_smpl in sample_names.items():
                new_fname = re.sub(old_smpl, new_smpl, new_fname)

        # если название такое же то ничего не делаем
        if new_fname == fname:
            continue
        old_put = os.path.join(dir, fname)
        new_put = os.path.join(dir, new_fname)
        if to_replace == True:
            # переименовываем (старый файл пропадет)
            os.rename(old_put, new_put)
        else:
            # копируем, читаем старый файл и записываем в новый
            f_old = open(old_put, 'rb')
            data = f_old.read()
            f_old.close()
            f_new = open(new_put, 'wb')
            f_new.write(data)
            f_new.close()