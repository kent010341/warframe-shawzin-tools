from WarframeShawzin import Sheet, speed_changing

# This sheet is from https://www.youtube.com/watch?v=TLnvusCgHWE
canon_1 = '5hAAKAGSANhAUUAbKAiRAoUAvSA2EA9MBESBKRBSEBZKBgRBmMBuBB1JB8MCDKCKBCRECYKCeMCmKCsMCzJC6RDCMDJRDQKDXhDhKDpSDwhD2UD+KEFRENUEUSEbEEiMEpSEvRE3EE9KFERFLMFTBFaJFhMFnKFuBF1EF7KGCMGJKGPJGWMGeRGlMGsRG0KG8'

sheet = speed_changing(canon_1, rate=1/2)
print(sheet)
print(sheet.get_encoded_sheet())