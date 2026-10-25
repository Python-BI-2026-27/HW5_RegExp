import re
import os
import shutil

def translate_to_salt_language(text: str):
    pattern = r'([аеёиоуыэюяАЕЁИОУЫЭЮЯ])'
    return re.sub(pattern, r'\1с\1', text)


def get_chords(file_path: str):
    with open(file_path) as file: 
        text = file.read() 
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, text)
        my_chords = set(result)
    return my_chords

def rename_files(dir: str, 
                 pattern: str, 
                 new_pattern: str = "", 
                 sample_names: dict = {}, 
                 to_replace: bool = False):
    for filename in os.listdir(dir):
        if len(re.findall(pattern, filename)) > 0:
            new_name = ''
            if len(new_pattern) > 0: 
                new_name = re.sub(pattern, new_pattern, filename)
                if to_replace == True:
                    os.rename(os.path.join(dir,filename), os.path.join(dir,new_name))
                else:
                    shutil.copy(os.path.join(dir,filename), os.path.join(dir,new_name))
            if len(sample_names) > 0:
                for key in sample_names: 
                    if key in filename or key in new_name:
                        if len(new_name) > 0:
                            new_sample_name = os.path.join(dir, new_name.replace(key, sample_names[key], 1))
                            os.rename(os.path.join(dir,new_name),new_sample_name)
                        else:
                            new_filename = os.path.join(dir, filename.replace(key, sample_names[key], 1))
                            if to_replace == True:
                                os.rename(os.path.join(dir,filename),new_filename)
                            else:
                                shutil.copy(os.path.join(dir,filename), new_filename)