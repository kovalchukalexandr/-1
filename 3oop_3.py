original_sentence = 'SLOVO YES'

common_dictionary = ['A', 'B', 'C',
    'D', 'E', 'F',
    'G', 'H', 'I',
    'J', 'K', 'L',
    'M', 'N', 'O',
    'P', 'Q', 'R',
    'S', 'T', 'U',
    'V', 'W', 'X',
    'Y', 'Z', '0', '1', '2',
    '3', '4', '5',
    '6', '7', '8',
    '9', ' ']
morse_dictionary = ['.-', '-...', '-.-.',
    '-..', '.', '..-.',
    '--.', '....', '..',
    '.---', '-.-', '.-..',
    '--', '-.', '---',
    '.--.', '--.-', '.-.',
    '...', '-', '..-',
    '...-', '.--', '-..-',
    '-.--',  '--..',
    '-----',  '.----',  '..---',
    '...--', '....-', '.....',
    '-....',  '--...', '---..',
    '----.', ' ']

i = len(original_sentence)
j = 0
words_separator = []

while i > 0:
    s = 0
    while s < len(common_dictionary):
        if common_dictionary[s] == original_sentence[j]:
            words_separator.append(morse_dictionary[s])
        s += 1
    i -= 1
    j += 1

print(words_separator)

