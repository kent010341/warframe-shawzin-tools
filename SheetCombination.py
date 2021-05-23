from copy import deepcopy
from Sheet import Sheet

def sheet_combination(sheet1, sheet2, time_between=6):
    sheet1 = _sheet_transform(sheet1)
    sheet2 = _sheet_transform(sheet2)
    # the maximum of timestamp is 4095.
    # Check if it's greater than 4095 after adding.
    last_timestamp_sheet1 = sheet1.get_notes_list()[-1].get_timestamp()
    last_timestamp = last_timestamp_sheet1 \
         + sheet2.get_notes_list()[-1].get_timestamp() + time_between
    assert last_timestamp <= 4095, \
        'Combination process failed, time length too long' + \
        ' (last timestamp = {})'.format(last_timestamp)

    # Check if tone is the same
    assert sheet1.get_tone() == sheet2.get_tone(), \
        'tone of sheet1 ({}) is different from sheet2 ({})' \
        .format(sheet1.get_tone(), sheet2.get_tone())

    # copy sheet
    notes_list1 = deepcopy(sheet1.get_notes_list())
    notes_list2 = deepcopy(sheet2.get_notes_list())

    start_timestamp_sheet2 = last_timestamp_sheet1 + time_between
    
    # Since negative time_between is available, checking if the first
    # timestamp of new sheet2 is greater than the last timestamp of 
    # sheet1 is necessary.
    assert start_timestamp_sheet2 > last_timestamp_sheet1, \
        ('the first timestamp of new sheet2 ({}) must be greater than' \
            + 'the last timestamp of sheet1 ({}).') \
        .format(start_timestamp_sheet2, last_timestamp_sheet1)

    # adding sheet2 to sheet1
    for i in range(len(notes_list2)):
        note = notes_list2[i]
        note.set_timestamp(note.get_timestamp() + start_timestamp_sheet2)
        notes_list1.append(note)

    # set notes_list
    sheet1.set_notes_list(notes_list1)

    return sheet1

# provide multiple sheet combination
def multiple_sheet_combination(*sheets, time_between=6):
    if hasattr(time_between, '__iter__'):
        assert len(sheets)-1 == len(time_between), 'the length of time_between should be (number of sheets)-1'
    else:
        time_between = [time_between for _ in range(len(sheets)-1)]
    i_time_between = 0

    sheet_output = sheets[0]
    for i, sheet in enumerate(sheets[1:]):
        try:
            sheet_output = sheet_combination(sheet_output, sheet, time_between=time_between[i_time_between])
            i_time_between += 1
        except AssertionError as e:
            print('Exception occurs while processing multiple sheet combination.')
            print('stop at sheet index {}, error message: {}'.format(i+1, e))

            break

    return sheet_output

# change string into sheet
def _sheet_transform(sheet):
    if isinstance(sheet, str):
        sheet = Sheet(sheet)

    return sheet