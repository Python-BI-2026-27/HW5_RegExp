def to_salty_language(text):
    pattern = r'.*?[аеёиоуыэюяАЕЕЁИОУЫЭЮЯ]'
    findings = re.findall(pattern, text)
    final = re.split(pattern, text, maxsplit=0)
    res = ''
    for piece in findings:
        res += piece + 'с' + piece[-1]
    res += final[-1]
    return res


def extract_chords(file_path):
    pattern = r'[ABCDEFG]{1}.*?\b'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return set(re.findall(pattern, text))


def rename_files(dir_path, pattern, new_pattern=None, sample_names=None, to_replace=False):
    files = os.listdir(dir_path)
    filtered_files = re.findall(pattern, ''.join(str(files)))
    if new_pattern is not None:
        new_files = [re.sub(pattern, new_pattern, f) for f in files]
    else:
        new_files = filtered_files
    if sample_names:
        new_files = [sample_names.get(name, name) for name in new_files]
    for old_name, new_name in zip(files, new_files):
        os.rename(os.path.join(dir_path, old_name), os.path.join(dir_path, new_name))
