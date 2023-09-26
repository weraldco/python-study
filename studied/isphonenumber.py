def isPhoneNumber(text):
    #   Check if not 12 if yes return False
    if len(text) != 12:
        return False
    
    #   Check if position 1 to 3 is decimal if not False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        
    #   If not hypen the 4th character then False
    if text[3] != '-':
        return False
    
    #   
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
        
    return True


message = 'Call me at 415-555-1011 tomorrow tomo rrowtomorr owtomo rrowtomorrow omorrowto morr owto morrowtomorrow. 415-555-9999 is my office.'

for i in range(len(message)):

    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print('Done')