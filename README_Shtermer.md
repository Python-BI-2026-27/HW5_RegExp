# HW5 RegExp

Author-Vanessa Shtermer

## What is in this repo

- `HW5_RegExp_Tasks.ipynb` — notebook with tasks: part 1 (regular expressions) and part 3 (demo of functions at the end)
- `hw5_functions.py` — module with functions from part 2
- `fastqs/` — fastq files, files `WT_*` were made by `rename_files`
- `data/` — `phones.txt` and `song.txt` for the tasks


## Functions

Import:
```python
from hw5_functions import salty_language, get_chords, rename_files
```

### salty_language(text)

Translates text to "salty language": after every vowel it adds `с` and the same vowel again.
```python
salty_language('Я иду гулять в парк')
# 'Яся исидусу гусулясять в пасарк'
```
### get_chords(path)

Takes path to a file with song text and chords and returns a set of chords. Works with russian songs (in russian song only chords have latin letters).

```python
get_chords('data/song.txt')
# {'Am', 'Dm', 'E', 'C', 'G', 'F'}
```

### rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False)

Renames many files in a folder.

- `dir` — folder with files
- `pattern` — pattern to choose files (and this part is replaced)
- `new_pattern` — what to put instead of `pattern`, if it is None there is no renaming by pattern
- `sample_names` — dictionary to rename samples, it works after `new_pattern`
- `to_replace` — `True` rename files (old files are deleted), `False` copy files (default)

Example (like on the picture in the task):

```python
rename_files('fastqs',
             pattern=r'Mix-(G\d)_S\d+_L001_(R[12])_001',
             new_pattern=r'\1_\2',
             sample_names={'G1': 'WT_rep1', 'G2': 'WT_rep2'},
             to_replace=False)
# Mix-G1_S21_L001_R1_001.fastq -> G1_R1.fastq -> WT_rep1_R1.fastq
```

## 🎵 Music for checking

- [Vanessa Shtermer 浏阳河(Luyang river on Guzheng)](https://drive.google.com/file/d/19jexlgKlLIPe3kE-tQgG8dwiuXtYZWwX/view?usp=drivesdk) Sad, just like my homework...
- [ Вне смерти — Plamenev](https://music.yandex.com/album/11449584/track/68844236?utm_medium=copy_link&ref_id=23a5a91d-6a16-4be5-a6ba-9db10c182e80)