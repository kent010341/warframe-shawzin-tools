import numpy as np
from .core.Transform import sheet_transform

def speed_changing(sheet, rate):
    sheet = sheet_transform(sheet)
    notes_list = sheet.get_notes_list()

    # get all time intervals between notes
    time_intervals = list()
    for i in range(1, len(notes_list)):
        time_intervals.append(
            notes_list[i].get_timestamp() - notes_list[i-1].get_timestamp())

    time_intervals = np.array(time_intervals)
    time_intervals = time_intervals * rate

    # changing timestamp
    timestamp = 0
    for i in range(len(time_intervals)):
        timestamp += int(time_intervals[i])
        assert timestamp <= 4095, 'timestamp is greater than 4095.'
        notes_list[i+1].set_timestamp(timestamp)

    sheet.set_notes_list(notes_list)

    return sheet