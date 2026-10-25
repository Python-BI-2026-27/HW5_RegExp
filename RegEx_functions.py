import re
import os

#Salty language translator
def salty_lang(string):
    for letter in 'аоуеыэёяиюАОУЕЫЭЁЯИЮ':
        string = re.sub(letter, letter + 'с' + letter.lower(), string)
    return(string)

#Chords extractor
def chords_extractor(file):
    with open(file) as file:
        pattern = r'[A-Z]{1}[^\s]*'
        all_chords = set()
        for line in file:
            chords = re.findall(pattern, line)
            all_chords.update(chords)
    return all_chords

#Rename files
def rename_files(dir,
                 pattern,
                 sample_names = None,
                 new_pattern = None,
                 to_replace = False):
    files = os.listdir(dir)
    for file in files:
        old_path = os.path.join(dir, file)
        if re.search(pattern, file) is None:
            continue
        if os.path.isdir(old_path):
            continue
        if new_pattern is not None:
            file = re.sub(pattern, new_pattern, file)
        if sample_names is not None:
            for old_name, new_name in sample_names.items():
                file = file.replace(old_name, new_name)
        new_path = os.path.join(dir, file)
        if new_path == old_path:
            continue
        if to_replace:
            if os.path.isfile(new_path):
                raise Exception(f'File with new name {new_path} already exists! Choose another name')
            else:
                os.rename(old_path, new_path)
        else:
            with open(old_path) as initial_file:
                if not os.path.isfile(new_path):
                    with open(new_path, mode = 'w') as copied_file:
                        copied_file.write(initial_file.read())
                else:
                    raise Exception(f'File with new name {new_path} already exists! Choose another name')
    return 'Renaming finished!'