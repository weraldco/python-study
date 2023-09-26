student = {'Werald':
           {"Year Level": "4th Year", "Subject": "Computer Science"},
           'Saphe':
           { "Year Level": "3rd Year", "Subject": "Information Tech",},
           'Winwin': 
           {"Year Level": "4th Year", "Subject": "Business Mngmnt",},
           }
print('Name'.ljust(15) + 'Year Level'.ljust(15) + 'Subject'.ljust(20))

for k,v in student.items():
   print(k.ljust(15) + v.get('Year Level').ljust(15) + v.get('Subject').ljust(20))