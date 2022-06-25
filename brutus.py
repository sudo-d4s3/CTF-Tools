ciphertxt = "The Quick Brown Fox Jumps Over The Lazy Dog"

def rot(sentence, rotn):
    d = {}
    for ascii_code in (65, 97):
        for alphabet_index in range(26):
            d[chr(ascii_code + alphabet_index)] = \
                        chr(ascii_code + (alphabet_index + rotn) % 26)
    return ''.join([d.get(letter, letter) for letter in sentence])

for i in range(1,27):
    print('Rot' + str(i) + ': ' + rot(ciphertxt,i))
