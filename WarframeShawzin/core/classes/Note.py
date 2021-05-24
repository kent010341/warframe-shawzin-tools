from ..EncoderDecoder import decode_timestamp, encode_timestamp
from ..Attributes import NOTE_LIST

class Note:
    def __init__(self, note_code):
        # check 3 letters
        assert len(note_code) == 3, 'note sould be 3 letters.'
        # check first word
        assert note_code[0] in NOTE_LIST, \
            'first letter {} isn\'t available'.format(note_code[0])

        # first letter is note
        self._note = note_code[0]
        # decoding timestamp to integer
        self._encoded_timestamp = note_code[1:]
        self._timestamp = decode_timestamp(self._encoded_timestamp)

    def __str__(self):
        return '{' + ('note: {}, timestamp: {}' \
            .format(self._note, self._timestamp)) + '}'

    # getter and setter
    def get_note(self):
        return self._note

    def get_timestamp(self):
        return self._timestamp

    def set_timestamp(self, timestamp):
        if isinstance(timestamp, int):
            self._timestamp = timestamp
            self._encoded_timestamp = encode_timestamp(self._timestamp)
        else:
            return

    def get_encoded_timestamp(self):
        return self._encoded_timestamp

    def set_encoded_timestamp(self, timestamp):
        if isinstance(timestamp, str):
            self._encoded_timestamp = timestamp
            self._timestamp = decode_timestamp(self._encoded_timestamp)
        else:
            return