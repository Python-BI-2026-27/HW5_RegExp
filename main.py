def rus_to_saulty(text: str) -> str:
    '''
    Translates text in Russian to 'saulty' language. 
    Looks for a vowel letter, writes consonant letter 'с'
    followed with that vowel letter in a word.
    Ex: 'Собака' -> 'Сособасакаса'

    Arguments:
    text: str, Russian text to translate to 'saulty'
    Returns str
    '''
    import re
    sault = re.sub(r'([аеёиоуыэюяаеёиоуыэюя])',
                   # vowel letter + 'c' + vovwel letter
                   lambda m: f"{m.group(1)}с{m.group(1).lower()}",
                   text, flags=re.IGNORECASE)
    return sault

def chords(path: str) -> set:
    '''
    Reads txt file with song music and chords and extracts 
    set of chords. Applies only with songs in Russian.

    Looks for the following patterns:
    main notes: A-H
    optional symbols: # and b
    optional chords types: m, m7, 7, maj7, add, sus (with optional digits), dim, aug 
    jazz and rock chords: C5, E5, C9, C11, etc.

    Arguments:
    path: str, path to a txt file with song chords

    Returns set of chords
    '''
    import re

    chord_pattern = r'\b[A-H][#b]?(?:m|m7|7|maj7|add\d+\sus\d?|dim|aug)?(?:\d{1,2})?\b'
    chords = set()

    with open(path, 'r') as file:
            for line in file:
                chord = re.findall(chord_pattern, line)
                if chord:
                    chords.update(chord)
    
    return chords


def rename_files(dir: str, pattern: str, new_pattern: str = None,
                 sample_names: dict[str, str] = None, to_replace: bool = False) -> list[str]:
   
    '''
    Chooses file in a directory accroding to search pattern.
    Renames or copies files in a directory according to
    1. New pattern, if specified.
    2. Dictionary with rules for name changing, if specidies.
    3. If both are specified, dictionary applies only after new pattern.

    Arguments:
    dir: str, directory with files to look for and process
    pattern: str, pattern to choose files in a directory
    new_pattern: str, pattern to use for file name changing, optional
    sample_names: dict[str,str], dictionary for file name changing, optional
    to_replace: if True, original files are renamed (removed), 
    if False (default value), original files are kept with old names and
    are copied with new names.

    Returns
    list[str]: new file names of the processed files
    '''
    import os
    import re
    import shutil

    new_files = [] # empty list
    
    files = os.listdir(dir) # files to choose in the directory
    for old_file in files:
        if not re.search(pattern, old_file):
            continue
        
        new_file = old_file

        # changing file name with a new_pattern
        if new_pattern:
            new_file = re.sub(pattern, new_pattern, new_file)
            
        # changing files with a sample name dictionary
        if sample_names:
            for old_name, new_name in sample_names.items():
                new_file = new_file.replace(old_name, new_name)

        if new_file == old_file:
            continue

        old_path = os.path.join(dir, old_file)
        new_path = os.path.join(dir, new_file)
        
        if to_replace:
            os.rename(old_path, new_path) #renaming old files
        else:
            shutil.copy(old_path, new_path) # copying files with new names

        new_files.append(new_file)

    return new_files
    