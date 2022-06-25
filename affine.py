#Atbash 
#a = 25
#b = 25
cipher = 'Ctoox'
a = 0 
b = 0

def affine(s, a, b):
    d = {}
    for ascii_code in (65, 97):
        for alphabet_index in range(26):
            d[chr(alphabet_index + ascii_code)] = chr(((a*alphabet_index+b)%26)+ascii_code)
    return ''.join([d.get(l,l) for l in s])

#affine(cipher, a, b)

for x in range(26):
    for y in range(26):
        print("A = " + str(x).zfill(2) + "; B = " + str(y).zfill(2) + ": " + affine(cipher,x,y))
