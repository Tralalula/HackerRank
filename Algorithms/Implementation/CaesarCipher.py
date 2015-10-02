import string

lettersLowercase = string.ascii_lowercase
lettersUppercase = string.ascii_uppercase

numLetters = len(lettersLowercase)
N = int(raw_input())
S = raw_input()
K = int(raw_input())

s = ""
for _ in S:
    if _.isalpha():
        if _.isupper():
            i = lettersUppercase.find(_)
            s += lettersUppercase[(i + K) % numLetters]
        else:
            i = lettersLowercase.find(_)
            s += lettersLowercase[(i + K) % numLetters]
    else:
        s += _

print s