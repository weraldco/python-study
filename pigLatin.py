# TEXT      : My name is AL SWEIGART and I am 4,000 years old.
# RESULT    : Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.

message = "My name is AL SWEIGART and I am 4,000 years old."
VOWEL = ('a' ,'e' ,'i' ,'o' ,'u' ,'y')

PigLatin = []

for word in message.split(' '):
    # Get all non letter
    prefixNonLetter = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetter += word[0]
        word = word[1:]
    
    if len(word) == 0:
        PigLatin.append(prefixNonLetter)
        continue

    # Get all non letter at the end of word
    suffixNonLetter = ''
    while len(word) > 0 and not word[-1].isalpha():
        suffixNonLetter += word[-1]
        word = word[:-1]
   
    isUpper = word.isupper() # check if it is uppercare
    isTitle = word.istitle() # check if it is title
    
    word = word.lower() # Lower the letter    

    prefixNotVowel = ''
    while len(word) > 0 and not word[0] in VOWEL:
        prefixNotVowel += word[0] 
        word = word[1:]

    if prefixNotVowel != '':
        newWord = word + prefixNotVowel + 'ay'
    else:
        newWord = word  + 'yay'

    if isUpper:
        newWord = newWord.upper()
    if isTitle:
        newWord =  newWord.title()
    
    newWord += suffixNonLetter

    PigLatin.append(newWord)

print(' '.join(PigLatin))

    