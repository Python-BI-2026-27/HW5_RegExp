##  Regular expressions

The module `finctions.py` contains two functions: `make_text_salty` and `get_chords`.

1. The `make_text_salty` creates the salty version of Russian text. 
The function takes a string of a Russian text as input and performs a modification: after each vowel, the consonant "s" is added, followed by the same vowel once more.
2. The `get_chords` extracts chords from a song lyrics file. 
The chords for each line must be placed on the preceding line and written as two-letter abbreviations.

### How to use:
```python
from functions import make_text_salty
```

```python
from functions import get_chords
```
### Examples:

In:
```python
make_text_salty('Как работает эта функция?')
```
Out:
```python
'Касак расабосотасаесет эсэтаса фусункцисияся?'
```

In:
```python
get_chords('data/song.txt')
```
Out:
```python
{'Am', 'C', 'Dm', 'E', 'F', 'G'}
```

Psss, here is some music:
 - Ranta, Miroshin - Jane Fraser (Journey of the Soul)
 - Aso - Seasons