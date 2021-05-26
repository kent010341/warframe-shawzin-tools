from ..EncoderDecoder import encode_notes_list
from .Note import Note

class Sheet:
    def __init__(self, sheet_str):
        self._encoded_sheet = sheet_str
        # first digit is scale
        self._scale = int(self._encoded_sheet[0])
        self._sheet_str = self._encoded_sheet[1:]
        # check if scale is available
        assert self._scale <= 9 and self._scale >= 1, \
            'scale should be an integer between 1 to 9'
        # check if sheet_str is multiple of 3
        assert len(self._sheet_str)%3 == 0, 'sheet_str should be multiple of 3'

        # list of notes
        self._notes_list = list()
        self._parsing()

    def __str__(self):
        output_str = 'scale: {}, notes: [\n'.format(self._scale)
        for note in self._notes_list:
            output_str += '{},\n'.format(str(note))

        return output_str + ']'

    # parsing sheet string
    def _parsing(self):
        for i in range(int(len(self._sheet_str)/3)):
            self._notes_list.append(Note(self._sheet_str[i*3: i*3+3]))

    # getter and setter
    def get_notes_list(self):
        return self._notes_list

    def set_notes_list(self, notes_list):
        self._notes_list = notes_list
        self._encoded_sheet = str(self._scale) + \
            encode_notes_list(self._notes_list)

    def get_scale(self):
        return self._scale

    def set_scale(self, scale):
        self._scale = scale

    def get_encoded_sheet(self):
        return self._encoded_sheet
