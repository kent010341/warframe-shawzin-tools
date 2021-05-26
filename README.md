# warframe-shawzin-tools Project

## Description
This project is made for dealing with the encoding Shawzin sheet music in Warframe game.

---

## Requirements
* Python 3.6 or above
* Numpy

---

## Demo Files
Files start with `demo_` are the demos.
* demo_sheet_combination.py
  * demo of `sheet_combination` and `multiple_sheet_combination`.

---

## WarframeShawzin Documentation

### Class: Sheet
#### Methods
* Constructor: `Sheet(sheet_str)`
  * `sheet_str` is the encoded string used in Warframe.
  * Initialize a `Sheet` object.
* `get_notes_list()`
  * Getter of list of notes (type of notes is `Note`).
* `set_notes_list(notes_list)`
  * Setter of list of notes (type of notes is `Note`).
  * `notes_list` should be a `list` of `Note` objects.
* `get_tone()`
  * Getter of `tone` which is the first character of the encoded sheet music.
* `set_tone(tone)`
  * Setter of `tone`. Must be 1 $\le$ `tone` $/le$ 9.
* `get_encoded_sheet()`
  * Getter of encoded sheet.

### Class: Note
> Currently only used in class `Sheet`. 
#### Method
* Constructor: `Note(note_code)`
  * `note_code` is the encoded string used in Warframe.
  * Initialize a `Note` object and decode as well.
* `get_note()`
  * Getter of the `note`.
* `get_timestamp()`
  * Getter of timestamp.
* `set_timestamp(timestamp)`
  * Setter of timestamp.
  * timestamp must be `str` type which means encoded.
* `get_encoded_timestamp()`
  * Getter of encoded timestamp.
* `set_encoded_timestamp(timestamp)`
  * Setter of encoded timestamp.
  * timestamp must be `int` type which means decoded.

### Methods
* `sheet_combination(*sheets, time_between=6)`
  * Combine multiple sheet music together, returning a `Sheet` object.
  * `*sheets` can be `str` or `Sheet` type.
  * `time_between` is the time between two `Sheet`, it can be an iterable object with `int`s (like `tuple` or `list`), and its length should match the number of `*sheets`-1.
* `speed_changing(sheet, rate)`
  * Changing speed of a sheet (making it faster is same as increasing its bpm).
  * `sheet` can be `str` or `Sheet` type.
  * `rate` can be `float` or `int`.