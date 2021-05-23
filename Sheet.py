from TimestampCoder import decode_timestamp
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
        self._timestamp = decode_timestamp(note_code[1:])

    def __str__(self):
        return 'note: {}, timestamp: {}'.format(self._note, self._timestamp)

    # getter of timestamp
    def get_timestamp(self):
        return self._timestamp

# Sheet Class
class Sheet:
    def __init__(self, sheet_str):
        # first digit is tone
        self._tone = int(sheet_str[0])
        self._sheet_str = sheet_str[1:]
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

    # getter of notes_list
    def get_notes_list(self):
        return self._notes_list

    # getter of tone
    def get_tone(self):
        return self._tone