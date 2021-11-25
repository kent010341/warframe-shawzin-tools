from ..EncoderDecoder import encode_notes_list
from ..Attributes import SCALE_DICT
from .Note import Note

class Sheet:
    def __init__(self, *args):
        if len(args) == 1:
            sheet_obj = args[0]
            if isinstance(sheet_obj, str):
                self._encoded_sheet = sheet_obj
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
            else:
                raise Exception("The parameter type {} used for constructor of Sheet is unacceptable.".format(type(sheet_obj)))

        elif len(args) == 2:
            if isinstance(args[1], list):
                self._scale = args[0]
                self._notes_list = args[1]
            else:
                raise Exception("The parameter type {} used for constructor of Sheet is unacceptable.".format(type(sheet_obj)))
        else:
            raise Exception("The number of parameters {} used for constructor of Sheet is unacceptable.".format(len(args)))

    def __str__(self):
        output_str = 'scale: {}, notes: [\n'.format(SCALE_DICT[self._scale])
        for note in self._notes_list:
            output_str += '{},\n'.format(note.to_string(self._scale))
        # remove last comma
        output_str = output_str[:-2] + '\n'

        return output_str + ']'

    def __getitem__(self, key):
        # slicing
        if isinstance(key, slice):
            new_sheet = self.clone()
            notes_list = new_sheet.get_notes_list()
            notes_list = notes_list[key]
            new_sheet.set_notes_list(notes_list)

            return new_sheet
        else:
            return self._notes_list[key]

    # parsing sheet string
    def _parsing(self):
        for i in range(int(len(self._sheet_str)/3)):
            self._notes_list.append(Note(self._sheet_str[i*3: i*3+3]))

    # clone a new sheet obj
    def clone(self):
        return Sheet(self._scale, self._notes_list)

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
