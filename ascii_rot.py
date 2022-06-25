def rot(s,n):
    #ascii table in order
    x = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

    #Builds the rotated dictionary
    d = {}
    rotated_x = x[n:] + x[:n]
    for i in range(94):
        d[33+i] = rotated_x[i]
    
    #Decodes text to ascii array
    s_codes = []
    for char in s:
        s_codes.append(ord(char))

    #Align ascii array to rotated dictionary
    output = ''
    for index in s_codes:
        output += d.get(index)

    return output

for i in range(1,94):
    print('Rot' + str(i) + ': ' + rot("~!",i))
