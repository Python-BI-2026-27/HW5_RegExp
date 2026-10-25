def rename_files(dir, pattern = r'Mix-|_S\d{2}_L\d{3}|_\d{3}', new_pattern = '', sample_names = None,  to_replace = False):
    import os
    import re
    import shutil
    if sample_names is None:
        sample_names={'G1': 'WT_rep1', 'G2': 'WT_rep2'}
    files = os.listdir(dir)
    for file in files:
        new_name = file
        new_name = re.sub(pattern, new_pattern, new_name)
        for key in sample_names:
            if new_name[0:2] == key:
                final_name = new_name.replace(key, sample_names[key])
                old = os.path.join(dir, file)
                new = os.path.join(dir, final_name)
                if to_replace: 
                    os.rename(old, new)
                else:
                    shutil.copy(old, new)

def salt_translate(text, pattern = r'[^аеёиоуыэюя\s]*[аеёиоуыэюя]|[^аеёиоуыэюя\s]+|\s+'):
    import re
    result = ''
    syllable = re.findall(pattern, text)
    for syl in syllable:
        if syl[-1] in 'аеёиоуыэюя':
            result += syl + 'с' + syl[-1]
        else:
            result += syl
    return result 

def extract_chords(file_path):
    with open(file_path) as file:
        text = file.read()
    import re
    pattern = r'\b[A-G]m?\b'
    chords = set(re.findall(pattern, text))
    return chords 