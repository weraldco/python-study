#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

# Convert this list and put bullet (*) in front of the group of text
textCopied = pyperclip.paste()

itemInText = textCopied.split('\n')

formatedText = []
for i, text in enumerate(itemInText):
    formatedText.append('* ' + text)

pyperclip.copy('\n'.join(formatedText))
