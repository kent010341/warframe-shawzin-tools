from Attributes import DECODE_DICT

# convert string to integer
def decode_timestamp(timestamp):
    # last letter
    decoded_timestamp = DECODE_DICT[timestamp[1]]
    # first letter
    decoded_timestamp += DECODE_DICT[timestamp[0]] * 64

    return decoded_timestamp

# convert integer to string
def encode_timestamp(timestamp):
    return '{}{}'.format(int(timestamp/64), timestamp%64)

# encoding notes_list to encoded sheet
def encode_notes_list(notes_list):
    encoded_sheet = ''

    for note in notes_list:
        encoded_sheet += '{}{}'.format(
                note.get_note(),
                note.get_encoded_timestamp()
            )

    return encoded_sheet