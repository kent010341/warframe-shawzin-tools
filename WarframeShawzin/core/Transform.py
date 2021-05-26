from .classes.Sheet import Sheet

# change string into sheet
def sheet_transform(sheet):
    if isinstance(sheet, str):
        sheet = Sheet(sheet)

    return sheet