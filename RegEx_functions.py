import re
import os

#Salty language translator
def salty_lang(string: str) -> str:
    """
    Translates any text in Russian to salty language

    Argument:
    string: str. Text in Russian
    
    Returns string translated to salty language
    """
    for letter in 'аоуеыэёяиюАОУЕЫЭЁЯИЮ':
        string = re.sub(letter, letter + 'с' + letter.lower(), string)
    return(string)

#Chords extractor
def chords_extractor(file: str) -> set[str]:
    """
    Extracts all unique chords present in input text file with song in Russian

    Argument:
    file: str. Path to a text file containing lyrics in Russian with chords in Latin
    
    Returns set of chords
    """
    with open(file) as file:
        pattern = r'[A-Z]{1}[^\s]*'
        all_chords = set()
        for line in file:
            chords = re.findall(pattern, line)
            all_chords.update(chords)
    return all_chords

#Rename files
def rename_files(dir: str,
                 pattern: str,
                 sample_names: dict[str, str] | None = None,
                 new_pattern: str | None = None,
                 to_replace: bool = False) -> str:
    """
    Finds all files in input directory which match the pattern, replaces names of files using new pattern and/or dictionary with new names. Could rename the existing files of create copies new names

    Arguments:
    dir: str. Input directory
    pattern: str. Pattern to find files
    sample_names = dict or None. Optional, use to rename files using fixed rules
    new_pattern = str or None. Optional, use to rename files using this pattern
    to_replace = bool. Default - False. If False creates copies of files with new names, if True renames existing files
    
    Returns 'Renaming finished!' in case of correct execution
    Raises exception in case if new files already exists
    """
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