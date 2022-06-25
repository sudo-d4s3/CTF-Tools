ciphertxt = "~!"

def rot(sentence, rotn):
    d = {}
    for ascii_code in (65, 97):
        for alphabet_index in range(26):
            d[chr(ascii_code + alphabet_index)] = \
                        chr(ascii_code + (alphabet_index + rotn) % 26)
    return ''.join([d.get(letter, letter) for letter in sentence])

def rot47(s):
    d = {}
    for index in range(33,127):
        d[chr(index)] = chr(33 + (index + 14) % 94)
    return ''.join([d.get(letter, letter) for letter in s])

for i in range(1,27):
    print('Rot' + str(i) + ': ' + rot(ciphertxt,i))

print('Rot47: ' + rot47(ciphertxt))
