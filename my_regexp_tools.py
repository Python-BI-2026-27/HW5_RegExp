import re
import os

def get_chords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    pattern = r'[a-zA-Z]+[^x2\n]'
    chords = re.findall(pattern, text)
    return set(chords)

def to_salty_language(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = []
    for char in text:
        if char in vowels:
            result.append(char)
            result.append("с")
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)

def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    all_files = os.listdir(dir)
    for filename in all_files:
        if not re.search(pattern, filename):
            continue
        
        new_name = filename
        
        if new_pattern is not None:
            new_name = re.sub(pattern, new_pattern, new_name)
        
        if sample_names is not None:
            for old_sample, new_sample in sample_names.items():
                if old_sample in new_name:
                    new_name = new_name.replace(old_sample, new_sample)

        full_old_path = os.path.join(dir, filename)
        full_new_path = os.path.join(dir, new_name)
        
        if os.path.exists(full_new_path):
            continue
        
        if to_replace:
            os.rename(full_old_path, full_new_path)
        else:
            with open(full_old_path, 'rb') as file_in:
                data = file_in.read()
            with open(full_new_path, 'wb') as file_out:
                file_out.write(data)


    
