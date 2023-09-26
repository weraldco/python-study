message = "My name is AL SWEIGART and I am 4,000 years old."
# Output:
#    Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.

VOWELS = ('a','e','i','o','u','y') # Check for consonant

pigLatin = [] #store the converted message

for word in message.split():
    
    # Remove non letter at the start of the word
    prefixNonLetter = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetter += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetter)
        continue
    

    # Remove non letter at the end of the word
    suffixNonLetter = ''
    while not word[-1].isalpha():
        suffixNonLetter += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()


    prefixConsonants =''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    else:
        word+= "yay"


    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    pigLatin.append(prefixNonLetter + word + suffixNonLetter)

print(' '.join(pigLatin))