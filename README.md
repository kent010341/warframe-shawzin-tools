# warframe-shawzin-tools Project

## Description
This project is made for dealing with the encoding Shawzin sheet music in Warframe game.

## Files
* core/Attributes.py
  * Contains some constant variables used in other code.
* core/EncoderDecoder.py
  * Contains the encoder and decoder of timestamp and sheet music.
* core/classes/Sheet.py
  * Contains class `Sheet`.
* core/classes/Note.py
  * Contains class: `Note`.
* SheetCombination.py
  * Contains two methods used for combining two sheets together.
* demo_sheet_combination.py
  * demo of `sheet_combination` and `multiple_sheet_combination`.

---

## Class: Sheet
### Methods
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

---

## Class: Note
> Currently only used in class `Sheet`. 
### Method
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
---
## Methods
* `sheet_combination(sheet1, sheet2, time_between=6)`
  * Combine two sheet music together, returning a `Sheet` object.
  * `sheet1` and `sheet2` can be `str` or `Sheet` type.
  * `time_between` is the time between `sheet1` and `sheet2`.
* `multiple_sheet_combination(*sheets, time_between=6)`
  * Combine multiple sheet music together, returning a `Sheet` object.
  * `*sheets` can be `str` or `Sheet` type.
  * `time_between` is the time between two `Sheet`, it can be a iterable object with `int`s (like `tuple` or `list`), and its length should match the number of `*sheets`-1.
