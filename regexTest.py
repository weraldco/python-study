# Ideas for Similar Programs
# Identifying patterns of text (and possibly substituting them with the sub()
# method) has many different potential applications. For example, you could:

# • Find website URLs that begin with http:// or https://.
# • Clean up dates in different date formats (such as 3/14/2019, 03-14-2019,
# and 2015/3/19) by replacing them with dates in a single, standard format.

import re
import pyperclip

copiedText = pyperclip.paste()

# urlRegex = re.compile(r'(http://|https://)(www\.)([a-zA-Z0-9]+)(\.[a-zA-Z]+)')
# for website in urlRegex.findall(copiedText):
#     print(''.join(website))

#'This is my website https://www.pooered.com asdasd This is my website https://www.werald.com asdasd'


dateRegex = re.compile(r'(\d{1,4})(-|/)(\d{1,2})(-|/)(\d{2,4})')
newSet = []
for date in dateRegex.findall(copiedText): 
    
    
    dateJoin = ''.join(date)
    if '-' in dateJoin:
        dt = dateJoin.split('-')
    elif '/' in dateJoin:
        dt = dateJoin.split('/')
    test_date = [0,0,0]
    
    for i in range(len(dt)):
        if len(dt[i]) == 4: # year
            test_date[2] = dt[i]

        elif len(dt[i]) == 2 and int(dt[i]) > 12: #month
            test_date[1] = dt[i]

        else:
            if len(dt[i]) == 1:
               test_date[0] = '0' + dt[i]
            else:
                test_date[0] =  dt[i]

    stringDate = '/'.join(test_date)
    newSet.append(stringDate)
        
print('\n'.join(newSet)) 
    