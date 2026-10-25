# HW5: Regular Expressions and File Processing

A set of Python functions for the HW5 assignment on regular expressions: transliteration of Russian text, chord extraction from a text file, and renaming of files.

Author:
* Angelina Popova

## Project Structure

```text
HW5_RegExp/
├── data/                    # data for the tasks
├── fastqs/                  # source fastq files for renaming
│   ├── Mix-G1_S21_L001_R1_001.fastq
│   ├── Mix-G1_S21_L001_R2_001.fastq
│   ├── Mix-G2_S22_L001_R1_001.fastq
│   └── Mix-G2_S22_L001_R2_001.fastq
├── img/                     # images for the notebook
├── HW5_RegExp_Tasks.ipynb   # notebook with task solutions and usage examples
├── main.py                  # module with the functions
└── README.md                # description
```

---

## Features & Functions

### 1. Russian to 'Saulty' Language Translator
Translates regular Russian text into the playful "saulty" (солёный) language by appending the consonant 'с' and repeating the original vowel after every vowel found.

* **Function**: `rus_to_saulty(text: str) -> str`
* **Example**: 
  ```python
  rus_to_saulty("Собака") # Returns: "Сособасакаса"
  ```

### 2. Music Chords Extractor
Reads a `.txt` text file containing a song's lyrics and musical notation, then extracts all unique Russian-style musical chords (supporting main notes A-H, accidentals `#`/`b`, common qualities like `m`, `m7`, `maj7`, `dim`, `aug`, and power/jazz chords like `C5`, `E5`, `C9`).

* **Function**: `chords(path: str) -> set`
* **Example**:
  ```python
  unique_chords = chords("data/song.txt")
  print(unique_chords) # Returns: {'Am', 'C', 'G', 'F7'}
  ```

### 3. File Renamer
Filters files inside a directory using a regex pattern and processes them using a new naming pattern, a direct mapping dictionary, or both. It can either modify files in-place or generate copies.

* **Function**: `rename_files(dir: str, pattern: str, new_pattern: str = None, sample_names: dict[str, str] = None, to_replace: bool = False) -> list[str]`
* **Parameters**:
  * `dir`: Target directory path.
  * `pattern`: Regex pattern used to match target files.
  * `new_pattern`: Regex substitution replacement pattern (optional).
  * `sample_names`: A look-up dictionary for substring replacement rules (optional).
  * `to_replace`: If `True`, original files are renamed. If `False`, copies with the new names are created alongside the originals.

!['rename_files'](img/rename_files.png)

---

## Prerequisites
* Python 3.x
* Standard built-in modules used: `re`, `os`, `shutil`

### Usage
Import the functions directly from `main.py` inside your script or your Jupyter Notebook:


---

## Music

Couple of songs I can't stop listening to recently:

* [Patrick Watson - Melody Noir](https://www.youtube.com/watch?v=MF-6mBuSGos&list=RDMF-6mBuSGos&start_radio=1)
* [Дайте танк (!) - Фамилия](https://www.youtube.com/watch?v=thHvFC3V22c&list=RDthHvFC3V22c&start_radio=1)
