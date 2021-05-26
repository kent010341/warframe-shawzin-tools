# available note
NOTE_LIST = ['B', 'C', 'E', 'J', 'K', 'M', 'R', 'S', 'U', 'h', 'i', 'k']

# use for decoding timestamp
DECODE_DICT = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63}

# Note Transform
NOTE_DICT = {
    1: {'B': 'lC', 'C': 'lD#', 'E': 'lF', 'J': 'lG', 'K': 'lA#', 'M': 'mC', 'R': 'mD#', 'S': 'mF', 'U': 'mG', 'h': 'mA#', 'i': 'hC', 'k': 'hD#'},
    2: {'B': 'lC', 'C': 'lD', 'E': 'lE', 'J': 'lG', 'K': 'lA', 'M': 'mC', 'R': 'mD', 'S': 'mE', 'U': 'mG', 'h': 'mA', 'i': 'hC', 'k': 'hD'},
    3: {'B': 'lC', 'C': 'lC#', 'E': 'lD', 'J': 'lD#', 'K': 'lE', 'M': 'lF', 'R': 'lF#', 'S': 'lG', 'U': 'lG#', 'h': 'lA', 'i': 'lA#', 'k': 'lB'},
    4: {'B': 'lC', 'C': 'lD#', 'E': 'lF', 'J': 'lF#', 'K': 'lG', 'M': 'lA#', 'R': 'mC', 'S': 'mD#', 'U': 'mF', 'h': 'mF#', 'i': 'mG', 'k': 'mA#'},
    5: {'B': 'lC', 'C': 'lD', 'E': 'lE', 'J': 'lF', 'K': 'lG', 'M': 'lA', 'R': 'lB', 'S': 'mC', 'U': 'mD', 'h': 'mE', 'i': 'mF', 'k': 'mG'},
    6: {'B': 'lC', 'C': 'lD', 'E': 'lEb', 'J': 'lF', 'K': 'lG', 'M': 'lAb', 'R': 'lBb', 'S': 'mC', 'U': 'mD', 'h': 'mEb', 'i': 'mF', 'k': 'mG'},
    7: {'B': 'lC', 'C': 'lC#', 'E': 'lF', 'J': 'lF#', 'K': 'lA#', 'M': 'mC', 'R': 'mC#', 'S': 'mF', 'U': 'mF#', 'h': 'mA', 'i': 'hC', 'k': 'hC#'},
    8: {'B': 'lC', 'C': 'lDb', 'E': 'lE', 'J': 'lF', 'K': 'lG', 'M': 'lAb', 'R': 'lBb', 'S': 'mC', 'U': 'mDb', 'h': 'mE', 'i': 'mF', 'k': 'mG'},
    9: {'B': 'lC#', 'C': 'lD#', 'E': 'lF#', 'J': 'lG#', 'K': 'lA#', 'M': 'mC#', 'R': 'mD#', 'S': 'mF#', 'U': 'mG#', 'h': 'mA#', 'i': 'hC#', 'k': 'hD#'}
}

# Scale Transform
SCALE_DICT = {
    1: 'Pentatonic Minor (1)',
    2: 'Pentatonic Major (2)',
    3: 'Chromatic (3)',
    4: 'Hexatonic (4)',
    5: 'Major (5)',
    6: 'Minor (6)',
    7: 'Hirajoshi (7)',
    8: 'Phrygian (8)',
    9: 'Yo (9)'
}