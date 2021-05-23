from EncoderDecoder import decode_timestamp, encode_timestamp, encode_notes_list
from Attributes import NOTE_LIST

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

# Sheet Class
class Sheet:
    def __init__(self, sheet_str):
        self._encoded_sheet = sheet_str
        # first digit is tone
        self._tone = int(self._encoded_sheet[0])
        self._sheet_str = self._encoded_sheet[1:]
        # check if tone is available
        assert self._tone <= 9 and self._tone >= 1, \
            'tone should be an integer between 1 to 9'
        # check if sheet_str is multiple of 3
        assert len(self._sheet_str)%3 == 0, 'sheet_str should be multiple of 3'

        # list of notes
        self._notes_list = list()
        self.parsing()

    def __str__(self):
        output_str = 'tone: {}, notes: [\n'.format(self._tone)
        for note in self._notes_list:
            output_str += '{},\n'.format(str(note))

        return output_str + ']'

    # parsing sheet string
    def parsing(self):
        for i in range(int(len(self._sheet_str)/3)):
            self._notes_list.append(Note(self._sheet_str[i*3: i*3+3]))

    # getter and setter
    def get_notes_list(self):
        return self._notes_list

    def set_notes_list(self, notes_list):
        self._notes_list = notes_list
        self._encoded_sheet = str(self._tone) + \
            encode_notes_list(self._notes_list)

    def get_tone(self):
        return self._tone

    def set_tone(self, tone):
        self._tone = tone

    def get_encoded_sheet(self):
        return self._encoded_sheet
